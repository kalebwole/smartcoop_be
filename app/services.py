import random
import string
from flask import current_app
import hashlib
# from .models import db, CooperativeMember, MemberCooperative
def generate_coop_id():
    return ''.join(random.choices(string.hexdigits.lower(), k=10))

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def insert_cooperative(cooperativename, email, password ):
    # Check for duplicate cooperative name and email
    db = current_app.db
    check_query = "SELECT COUNT(*) FROM cooperative WHERE cooperativename = %s OR email = %s"
    if db.read(check_query, (cooperativename, email))[0]['COUNT(*)'] > 0:
        return {"error": "Cooperative name or email already exists"}

    coop_id = generate_coop_id()
    hashed_password = hash_password(password)
    query = """
    INSERT INTO cooperative (coop_id, cooperativename, email, password )
    VALUES (%s, %s, %s, %s)
    """
    params = (coop_id, cooperativename, email, hashed_password)
    
    try:
        cooperative_id = db.create(query, params)
        print("yes")
        return {"coop_id": coop_id, "cooperative_id": cooperative_id}
    except Exception as e:
        print(f"Error inserting cooperative: {e}")
        return {"error": "Error inserting cooperative"}

def verify_credentials(email, password):
    query = "SELECT id, cooperativename, email, password, coop_id FROM cooperative WHERE email = %s"
    db = current_app.db
    result = db.read(query, (email,))
    
    if result:
        user = result[0]
        stored_password = user['password']
        if stored_password == hash_password(password):
            return {
                "id": user['id'],
                "cooperativename": user['cooperativename'],
                "email": user['email'],
                "coop_id": user['coop_id']
            }
    
    return None
def create_member(fullname, email, phoneno, address, staff_id, dob, gender, cooperative_id):
    # Mock implementation assuming current_app.db is properly configured
    db = current_app.db
    
    # Check if member already exists
    check_query = "SELECT COUNT(*) FROM cooperative_members WHERE email = %s"
    if db.read(check_query, (email,))[0]['COUNT(*)'] > 0:
        return {"error": "Member already exists."}

    # Create new member record
    query = """
    INSERT INTO cooperative_members (fullname, email, phoneno, address, staff_id, dob, gender )
    VALUES (%s, %s, %s, %s, %s, %s,  %s)
    """
    params = (fullname, email, phoneno, address, staff_id, dob, gender)
    
    try:
        db.create(query, params)
        return {"message": "Member created successfully."}
    except Exception as e:
        print(f"Error creating member: {e}")
        return {"error": "Error creating member"}

def fetch_all_members():
    
    db = current_app.db
    query = "SELECT id, fullname, email, phoneno, address, staff_id, dob, gender  FROM cooperative_members"
    
    try:
        members = db.read(query)
        return members
    except Exception as e:
        print(f"Error fetching members: {e}")
        return {"error": "Error fetching members"}

def delete_member(member_id):
    # Mock implementation assuming current_app.db is properly configured
    db = current_app.db
    
    # Check if member exists
    check_query = "SELECT COUNT(*) FROM cooperative_members WHERE id = %s"
    if db.read(check_query, (member_id,))[0]['COUNT(*)'] == 0:
        return {"error": "Member not found."}

    # Delete the member record
    delete_query = "DELETE FROM cooperative_members WHERE id = %s"
    
    try:
        db.delete(delete_query, (member_id,))
        return {"message": "Member deleted successfully."}
    except Exception as e:
        print(f"Error deleting member: {e}")
        return {"error": "Error deleting member"}
