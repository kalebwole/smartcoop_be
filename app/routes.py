from flask import Blueprint, request, jsonify, render_template
from .services import insert_cooperative, verify_credentials, create_member, fetch_all_members, delete_member, create_loan_type,delete_loan_type,fetch_loan_types

main_bp = Blueprint('main', __name__)

###################################################### 
######################################################
# VIEWS ROUTES
###################################################### 
######################################################

@main_bp.route('/', methods=['GET'])
def hello():
    return render_template('default.html')

@main_bp.route('/sign-up', methods=['GET'])
def signupView():
    return render_template('signup.html')
@main_bp.route('/sign-in', methods=['GET'])
def signinView():
    return render_template('signin.html')
@main_bp.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('dashboard.html')
@main_bp.route('/dashboard/add_member', methods=['GET'])
def add_member():
    return render_template('add_member.html')
@main_bp.route('/dashboard/view_member', methods=['GET'])
def view_member():
    return render_template('view_member.html')
@main_bp.route('/dashboard/loan-type', methods=['GET'])
def LoanTypes():
    return render_template('manage-loan-type.html')

###################################################### 
######################################################
# API ROUTES
###################################################### 
######################################################

@main_bp.route('/cooperative/signup', methods=['POST'])
def add_cooperative():
    data = request.get_json()
    
    cooperativename = data.get('cooperativename')
    email = data.get('email')
    password = data.get('password')
    print(cooperativename,email,password)
  
    if not cooperativename or not email or not password:
        return jsonify({"error": "Cooperative name, email, and password are required"}), 400

    result = insert_cooperative(cooperativename, email, password )
    
    if 'error' in result:
        return jsonify(result), 400 if result['error'] == "Cooperative name or email already exists" else 500
    
    return jsonify({"message": "Cooperative added successfully", "coop_id": result['coop_id'], "cooperative_id": result['cooperative_id']}), 201

@main_bp.route('/cooperative/signin', methods=['POST'])
def sign_in():
    data = request.get_json()
    
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400
    
    user = verify_credentials(email, password)
    
    if user:
        return jsonify({
            "message": "Sign-in successful",
            "user": user
        }), 200
    else:
        return jsonify({"error": "Invalid email or password"}), 401
@main_bp.route('/cooperative/members/create', methods=['POST'])
def create_cooperative_member():
    data = request.get_json()
    
    fullname = data.get('fullname')
    email = data.get('email')
    phoneno = data.get('phoneno')
    address = data.get('address')
    staff_id = data.get('staff_id')
    dob = data.get('dob')
    gender = data.get('gender')
    cooperative_id = data.get('cooperative_id')

    if not all([fullname, email, phoneno, address, staff_id, dob, gender, cooperative_id]):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        result = create_member(fullname, email, phoneno, address, staff_id, dob, gender, cooperative_id)
        return jsonify(result), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@main_bp.route('/cooperative/members', methods=['GET'])
def get_all_members():
    members = fetch_all_members()
    
    if isinstance(members, list):
        return jsonify(members), 200
    else:
        return jsonify({"error": "Failed to fetch members"}), 500
@main_bp.route('/cooperative/members', methods=['DELETE'])
def deletemember():
    data = request.get_json()
    member_id = data.get('id')
@main_bp.route('/cooperative/loantype/create', methods=['POST'])
def create_loanType():
    data = request.get_json()
    
    title = data.get('title')
    interest_rate = data.get('interest_rate')
    loan_type = data.get('loan_type')
    availability = data.get('availability')
    coop_id = data.get('coop_id')
    
    if not all([title,interest_rate,loan_type,availability,coop_id]):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        result = create_loan_type(title,interest_rate,loan_type,availability,coop_id)
        return jsonify(result), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@main_bp.route('/cooperative/loantype', methods=['DELETE'])
def delete_loanType():
    data = request.get_json()
    
    id = data.get('id')
    
    if not all([id]):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        result = delete_loan_type(id)
        return jsonify(result), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@main_bp.route('/cooperative/loantype', methods=['POST'])
def get_loanType():
    data = request.get_json()
    
    coop_id = data.get('coop_id')
    page = data.get('page')
    per_page = data.get('per_page')
   
    if not all([coop_id, page, per_page]):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        result = fetch_loan_types(coop_id,page,per_page)
        return jsonify(result), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

