import random
import string
from flask import current_app
import hashlib
from datetime import datetime, timedelta
from .loans import straight_line_loan_schedule, straight_line_upfront_loan_schedule, reducingBalance_loan_schedule
# from .models import db, CooperativeMember, MemberCooperative
def generate_coop_id():
    return ''.join(random.choices(string.hexdigits.lower(), k=10))

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def insert_cooperative(cooperativename, email, password ):
  
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

def verify_credentials(email, password,typed):
    print(typed)
    if(typed=='member'):
        print("am here")
        query = "SELECT * FROM cooperative_members WHERE email = %s"
        db = current_app.db
        result = db.read(query, (email,))
        
        if result:
            user = result[0]
            stored_password = user['password']
            print(stored_password +" "+hash_password(password))
            if stored_password == hash_password(password):
                return {
                    "id": user['id'],
                    "fullname": user['fullname'],
                    "email": user['email'],
                    "staff_id": user['staff_id'],
                    "wallet":user['wallet']
                }
    
    else:
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
def create_member(fullname, email, phoneno, address, staff_id, dob, gender, cooperative_id, nok_name, nok_phone, nok_relationship, bank_name, account_number, sort_code, salary_number, password=None):
    # Mock implementation assuming current_app.db is properly configured
    db = current_app.db

    # Set default password if not provided
    default_password = "password"  # Replace with your desired default password
    if not password:
        password = default_password
    print(password)
    hashed_password = hash_password(password)

    # Check if member already exists
    check_query = "SELECT COUNT(*) FROM cooperative_members WHERE email = %s"
    if db.read(check_query, (email,))[0]['COUNT(*)'] > 0:
        return {"error": "Member already exists."}

    # Create new member record
    query = """
    INSERT INTO cooperative_members (fullname, email, phoneno, address, staff_id, dob, gender, nok_name, nok_phone, nok_relationship, bank_name, account_number, sort_code, salary_number, password)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    params = (fullname, email, phoneno, address, staff_id, dob, gender, nok_name, nok_phone, nok_relationship, bank_name, account_number, sort_code, salary_number, hashed_password)
    
    queryLoan = """
    INSERT INTO member_cooperatives (user_id, cooperative_id) VALUES (%s, %s)
    """
    paramsLoan = (staff_id, cooperative_id)
    
    try:
        db.create(query, params)
        db.create(queryLoan, paramsLoan)
        return {"message": "Member created successfully."}
    except Exception as e:
        print(f"Error creating member: {e}")
        return {"error": "Error creating member"}
def fetch_all_members(coop_id):
    
    db = current_app.db
    # print(coop_id)
    queryFetch = "SELECT user_id FROM member_cooperatives WHERE cooperative_id = %s"
    # print(queryFetch)
    params = (coop_id,)
    getIDS = db.read(queryFetch,params)
    # print(getIDS)
    IDS=""
    for each in getIDS:
        if IDS == "":
            IDS = each['user_id']
        else:
            IDS = IDS+","+each['user_id']
         
        


 
    string_list = IDS.strip(',').split(',')
    placeholders = ', '.join(['%s'] * len(string_list))
    query = f"SELECT id, fullname, email, phoneno, address, staff_id, dob, gender FROM cooperative_members WHERE staff_id IN ({placeholders})"
    # query = "SELECT id, fullname, email, phoneno, address, staff_id, dob, gender   FROM cooperative_members WHERE %s IN staff_id"
    print(query)
    try:
        # par = (IDS,)
        members = db.read(query, string_list)
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
def create_loan_type(title,interest_rate,loan_type,availability,coop_id,requiredAmount):
    # Mock implementation assuming current_app.db is properly configured
    db = current_app.db
    
    # Check if member already exists
    check_query = "SELECT COUNT(*) FROM coop_loantypes WHERE coop_id = %s and title = %s"
    if db.read(check_query, (coop_id,title,))[0]['COUNT(*)'] > 0:
        return {"error": "Loan type already exists."}

    # Create new member record
    query = """
    INSERT INTO coop_loantypes (title,interest_rate,loan_type,availability,coop_id,requiredAmount )
    VALUES (%s, %s, %s, %s, %s,%s)
    """
    params = (title,interest_rate,loan_type,availability,coop_id,requiredAmount)
    
    try:
        db.create(query, params)
        return {"message": "Loan Type Created created successfully."}
    except Exception as e:
        print(f"Error creating loan types: {e}")
        return {"error": "Error creating member"}

def create_savings_type(title,auto,coop_id):
    db = current_app.db
    
    # Check if member already exists
    check_query = "SELECT COUNT(*) FROM coop_savingstypes WHERE coop_id = %s and title = %s"
    if db.read(check_query, (coop_id,title,))[0]['COUNT(*)'] > 0:
        return {"error": "Loan type already exists."}

    # Create new member record
    query = """
    INSERT INTO coop_savingstypes (title,coop_id,auto_type)
    VALUES (%s, %s, %s)
    """
    params = (title,coop_id,auto)
    
    try:
        db.create(query, params)
        return {"message": "Savings Type Created created successfully."}
    except Exception as e:
        print(f"Error creating savings types: {e}")
        return {"error": "Error creating member"}
def delete_loan_type(id):
    
    db = current_app.db
    
    
    check_query = "SELECT COUNT(*) FROM coop_loantypes WHERE id = %s "
    if db.read(check_query, (id,))[0]['COUNT(*)'] == 0:
        return {"error": "Loan type not found."}

    # Delete the loan type record
    delete_query = "DELETE FROM coop_loantypes WHERE id = %s"
    print(delete_query)
    try:
        db.delete(delete_query, (id,))
        return {"message": "Loan type deleted successfully."}
    except Exception as e:
        print(f"Error deleting loan type: {e}")
        return {"error": "Error deleting loan type"}
def fetch_loan_types(coop_id, page=1, per_page=10):
     
    db = current_app.db
    
    
    offset = (page - 1) * per_page
    
    
    query = """
    SELECT * FROM coop_loantypes 
    WHERE coop_id = %s
    LIMIT %s OFFSET %s
    """
    
    params = (coop_id, per_page, offset,)
    # print(coop_id)  
    try:
        loan_types = db.read(query, params)
        return loan_types
    except Exception as e:
        print(f"Error fetching loan types: {e}")
        return []

def fetch_savings_types(coop_id, page=1, per_page=10):
     
    db = current_app.db
    
    
    offset = (page - 1) * per_page
    
    
    query = """
    SELECT * FROM coop_savingstypes 
    WHERE coop_id = %s
    LIMIT %s OFFSET %s
    """
    
    params = (coop_id, per_page, offset,)
    # print(coop_id)  
    try:
        loan_types = db.read(query, params)
        return loan_types
    except Exception as e:
        print(f"Error fetching loan types: {e}")
        return []


def loanCalculator(loanType,principal,tenure):
    db = current_app.db
    
    
    # offset = (page - 1) * per_page
    
    
    query = """
    SELECT * FROM coop_loantypes 
    WHERE id = %s
    """
    
    params = (loanType,)
    # print(loanType)  
    try:
        loan_types = db.read(query, params)
        interest = loan_types[0]['interest_rate']
        # print(loan_types[0]['loan_type'])
        if loan_types[0]['loan_type']=='straigthLine':
            calculateLoan = straight_line_loan_schedule(int(principal),int(tenure),int(interest))
            return calculateLoan
        elif loan_types[0]['loan_type']=='straigthLineUpfront':
            calculateLoan = straight_line_upfront_loan_schedule(int(principal),int(tenure),int(interest))
            return calculateLoan
        elif loan_types[0]['loan_type']=='reducing':
            calculateLoan = reducingBalance_loan_schedule(int(principal),int(tenure),int(interest))
            return calculateLoan

        
    except Exception as e:
        print(f"Error calcu: {e}")
        return []
    
def createLoan(staffId,coop_id,loanObject, loanType,LTObject):
    db = current_app.db
    try:
        # print(LTObject)

        principal =  0
        tenure = len(loanObject)
        total_interest = 0
        monthly_interest = 0
        monthly_repayment = 0
        amount_disbursed = 0
        amount_paid = 0
        total_loan = 0
        if(LTObject['loan_type']=='straigthLine'):
            principal = loanObject[0]['amount_received']
            total_interest = tenure * int(loanObject[1]['monthly_interest_repayment'])
            monthly_interest = int(loanObject[1]['monthly_interest_repayment'])
            amount_disbursed = int(loanObject[0]['amount_received'])
            total_loan = total_interest + amount_disbursed
            monthly_repayment = int(loanObject[1]['monthly_principal_repayment'])
        elif LTObject['loan_type']=='straigthLineUpfront':
            principal = loanObject[0]['remaining_principal']
            total_interest = loanObject[0]['monthly_interest_repayment']
            monthly_interest = loanObject[0]['monthly_interest_repayment'] / tenure
            amount_disbursed = loanObject[0]['amount_received']
            total_loan = loanObject[1]['remaining_principal']
            monthly_repayment = loanObject[1]['monthly_principal_repayment']
        elif LTObject['loan_type']=='reducing':
            principal = loanObject[0]['remaining_principal']
            total_interest = loanObject[1]['monthly_interest_repayment'] * tenure
            monthly_interest = loanObject[1]['monthly_interest_repayment'] 
            amount_disbursed = loanObject[0]['amount_received']
            total_loan = loanObject[0]['remaining_principal']
            monthly_repayment = loanObject[1]['monthly_principal_repayment']
        #  `coop_id`, `staff_id`, `principal`, `tenure`, `loan_type`, `total_interest`, `monthly_interest`, `monthly_repayment`, `amount_disbursed`, `amount_paid`, `total_loan`, `approved_status`, `approved_date`, `request_date`, `status`SELECT * FROM `loan_application` WHERE 1
        print(principal,total_interest,monthly_interest,amount_disbursed,total_loan)
        query = """
                INSERT INTO loan_application (loan_id,coop_id, staff_id, principal, tenure, loan_type, total_interest,monthly_interest,monthly_repayment, amount_disbursed,total_loan )
                VALUES (%s,%s, %s, %s, %s,%s, %s, %s, %s , %s, %s)
                """
        random_number = random.randint(1000000000, 9999999999)
        params = (random_number,coop_id, staffId, principal, tenure,loanType,total_interest,monthly_interest, monthly_repayment,amount_disbursed,total_loan )
        cooperative_id = db.create(query, params)
        
      
        return 0    

    except Exception as e:
        print(f"Error fetching loan types: {e}")
        return []
def fetch_loans(coop_id, page=1, per_page=10):
     
    db = current_app.db
    
    
    offset = (page - 1) * per_page
    
    
    query = """
    SELECT * FROM loan_application 
    WHERE coop_id = %s
    LIMIT %s OFFSET %s
    """
    
    params = (coop_id, per_page, offset)
    print(coop_id)  
    try:
        loan_types = db.read(query, params)
        return loan_types
    except Exception as e:
        print(f"Error fetching loan types: {e}")
        return []

def fetch_loans_user(coop_id, staff_id,page=1, per_page=10):
     
    db = current_app.db
    
    
    offset = (page - 1) * per_page
    
    print(staff_id)
    
    query = """
    SELECT * FROM loan_application 
    WHERE coop_id = %s and staff_id = %s
    LIMIT %s OFFSET %s
    """
    # return staff_id
    params = (coop_id,staff_id, per_page, offset,)
    # print(coop_id)  
    try:
        loan_types = db.read(query, params)
        response = []
        for eached in loan_types:

            newQuery = """
            SELECT * FROM coop_loantypes 
            WHERE id = %s
            """
            print(eached['loan_type'])
            # return staff_id
            paramsd = (str(eached['loan_type']),)
            loanTp = db.read(newQuery, paramsd)
            response.append({"loans":eached,"typeData":loanTp[0]})
        return response
    except Exception as e:
        print(f"Error fetching loan types: {e}")
        return []


def fetchAllloans(coop_id):
     
    db = current_app.db
    
    
    # offset = (page - 1) * per_page
    
    
    query = """
    SELECT * FROM loan_application 
    WHERE loan_id = %s
    
    """
    
    params = (coop_id,)
    # print(coop_id)  
    try:
        loan_types = db.read(query, params)
        return loan_types
    except Exception as e:
        print(f"Error fetching loans: {e}")
        return []

 

def update_loans(loan_id, type,loanType,principal,tenure,staff_id,coop_id):
    # print(type) 
    db = current_app.db
    # print(type)
    current_date = datetime.now().date()
    print(type)
    if(type=='approved'):
        # print("yes here")
        try:
            query = """
                UPDATE loan_application SET approved_status = 'approved', status = 'active',  approved_date = %s WHERE loan_id = %s 
            """
            newLoan = loanCalculator(loanType,principal,tenure)

            # print(query)
            createInstallment(newLoan,staff_id,coop_id,loan_id)
            params = (current_date, loan_id,)
            # print(params)
            loan_types = db.update(query, params)
            return loan_types
        except Exception as e:
            print(f"Error updating loan types: {e}")
            return []
        
    else:
        query = """
            UPDATE loan_application SET approved_status = 'rejected',  approved_date = %s WHERE loan_id = %s 
        """
        params = (current_date, loan_id,)
        loan_types = db.update(query, params)
        return "no"
    
    
    # print(coop_id)  
    # try:
       
        
    #     return loan_types
    # except Exception as e:
    #     print(f"Error updating loan types: {e}")
    #     return []
def createInstallment(loanObject,staff_id,coop_id,loan_id):
    db = current_app.db
    current_date = datetime.now().date()
    try:
        for each in loanObject:
            current_date = current_date + timedelta(days=30)
            query = """
                    INSERT INTO loan_payment_history (loan_id,amount_to_pay,amount_paid,staff_id,coop_id,next_due) VALUES
                    (%s,%s,%s,%s,%s,%s)
                    """
                
            params = (loan_id, each['monthly_repayment'], 0, staff_id, coop_id,current_date)
    
            db.create(query, params)
            # print(future_date)
        return 0
    except Exception as e:
        return []
def fetch_savings(coop_id,page,per_page):
    db = current_app.db
    
    
    offset = (page - 1) * per_page
    
    
    query = """
    SELECT * FROM coop_savings
    WHERE coop_id = %s
    LIMIT %s OFFSET %s
    """
    
    params = (coop_id, per_page, offset,)
    # print(coop_id)  
    try:
        loan_types = db.read(query, params)
        return loan_types
    except Exception as e:
        print(f"Error fetching loan types: {e}")
        return []

    
def newSavings(coop_id,user_id,amount,savings_type,channel):
    try:
        db = current_app.db
        query = """
                INSERT INTO coop_savings (coop_id, user_id, amount, savings_type, channel)
                VALUES (%s,%s, %s, %s, %s)
                """
        random_number = random.randint(1000000000, 9999999999)
        params = (coop_id,user_id,amount,savings_type,channel, )
        cooperative_id = db.create(query, params)
        # add to the users wallet
        getquery = """
                SELECT * FROM cooperative_members where staff_id = %s
                        """
        getParams = (user_id,)
        cooperative_id = db.read(getquery, getParams)
        # print(int(cooperative_id[0]['wallet']) + float(amount))
        walletUpdata  = int(cooperative_id[0]['wallet']) + float(amount)
        queryUpdate = """
                        UPDATE cooperative_members SET wallet = %s WHERE staff_id = %s
                    """
        paramsUpdate = (walletUpdata,user_id,)
        updateUsers = db.update(queryUpdate,paramsUpdate)


        # create transaction
        createtransactions(coop_id,user_id,amount,'credit','user - user','savings')
        return "Successful"
    except Exception as e:
        print(f"Error fetching loan types: {e}")
        return []

def getProfiles(user_id):
     
    db = current_app.db
    
    
    # offset = (page - 1) * per_page
    
    
    query = """
    SELECT * FROM  cooperative_members
    WHERE staff_id = %s
    
    """
    
    params = (user_id,)

    querySavings = """
        SELECT * FROM  coop_savings
    WHERE user_id = %s
        
    """
    paramSavings = (user_id,)

    queryLoans = """
        SELECT * FROM  loan_application
    WHERE staff_id = %s
        
    """
    paramLoans = (user_id,)
    # print(coop_id)  
    try:
        userData = db.read(query, params)
        savingsData = db.read(querySavings,paramSavings)
        loansData = db.read(queryLoans,paramLoans)


        return {"user":userData[0],"savings":savingsData,"loans":loansData}
    except Exception as e:
        print(f"Error fetching loan types: {e}")
        return []

def getCoopProfiles(user_id):
     
    db = current_app.db
    
    
    # offset = (page - 1) * per_page
    
    
    query = """
    SELECT * FROM  cooperative
    WHERE coop_id = %s
    
    """
    
    params = (user_id,)

     # print(coop_id)  
    try:
        userData = db.read(query, params)


        return {"coop":userData[0]}
    except Exception as e:
        print(f"Error fetching loan types: {e}")
        return []

def updateCoopProfiles(coop_id,cooperativename,email,registration_fee,phone,address,prefix,account_name,account_number,bank_name):
    db = current_app.db
    
    
    query = """
    UPDATE cooperative SET cooperativename = %s, email = %s, registration_fee = %s, phone = %s, address = %s, prefix = %s, account_name = %s, account_number = %s,   bank_name = %s WHERE coop_id = %s
    
    """
    
    params = (cooperativename,email,registration_fee,phone,address,prefix,account_name,account_number,bank_name,coop_id,)

     # print(coop_id)  
    try:
        userData = db.update(query, params)


        return {"message":"Updated Successfully"}
    except Exception as e:
        print(f"Error fetching loan types: {e}")
        return []
def fetchLoan(loan_id):
     db = current_app.db
     queryLoan = """
            SELECT * FROM  loan_application
            WHERE loan_id = %s
    
            """
     params = (loan_id,)
     queryLoanDetail = """
            SELECT * FROM  loan_payment_history
            WHERE loan_id = %s
    
            """
     try:
        loanData = db.read(queryLoan, params)
        detailData = db.read(queryLoanDetail,params)

        return {"coop":loanData[0],"repayment":detailData}
     except Exception as e:
        print(f"Error fetching loan types: {e}")
        return []

def createtransactions(coop_id, staff_id, amount, transaction_type,initiator,type):
     
    db = current_app.db
    
 
  
    query = """
    INSERT INTO transactions (coop_id, staff_id, amount, transaction_type,initiator,type)
    VALUES (%s, %s, %s, %s,%s,%s)
    """
    params = (coop_id, staff_id, amount, transaction_type,initiator,type)
    
    try:
        db.create(query, params)
    
        return {"message": "Transaction created successfully."}
    except Exception as e:
        print(f"Error creating transaction: {e}")
        return {"error": "Error creating transaction"}

def dashboard(coop_id):
     try:
        db = current_app.db
     
        # add to the users wallet
        getUsers = """
                SELECT count(id) as members,sum(wallet) as savings FROM cooperative_members where coop_id = %s
                        """
        getParamsUser = (coop_id,)
        getUsers = db.read(getUsers,getParamsUser)
 
        return "Successful"
     except Exception as e:
        print(f"Error fetching loan types: {e}")
        return []
# def creditWallet(staff_id,amount):
def repayLoan(loan_id,amount):
     try:
        db = current_app.db
     
        # add to the users wallet
        getLoanData = """
                SELECT * FROM loan_payment_history where loan_id = %s  and status = 'not paid'
                        """
        getParamsUser = (loan_id,)
        loanRepayment = db.read(getLoanData,getParamsUser)
        # print(loa)
        keptAmount = amount
        amountPaid = 0
        for each in loanRepayment:
            # print(keptAmount)
            if(keptAmount<=0):
                break
            else:
                
                if keptAmount > each['amount_to_pay']:
                    
                    # print(str(keptAmount) +" "+str(each['amount_to_pay']) +" "+str(amount))
                    currentID = each['id']
                    updateLoan = """
                                    UPDATE loan_payment_history SET amount_paid = %s, status  = 'paid' WHERE loan_id = %s and id = %s
                                        """
                    lph = (each['amount_to_pay'],loan_id,currentID)
                    amountPaid = amountPaid + each['amount_to_pay']
                    db.update(updateLoan,lph)
                    keptAmount = keptAmount - each['amount_to_pay']
                else:
                    # creditWallet(each['staff_id'],keptAmount)
                    newSavings(each['coop_id'],each['staff_id'],keptAmount,'loanBalance','wallet')
                    keptAmount = keptAmount - keptAmount
        # print(amountPaid)
        # get the loan data 
        getLoanDetail = """
                SELECT * FROM loan_application where loan_id = %s 
                        """
        getParamsDetail = (loan_id,)
        loanDeatils = db.read(getLoanDetail,getParamsDetail)
        # add the amount paid
        status = "active"
        amountTotal = loanDeatils[0]['amount_paid'] + amountPaid
        # print(str(amountTotal +" "+ str(loanDeatils[0]['amount_paid'])))
        # print(str(amountTotal) +" "+str(amountPaid))
        # print(loanDeatils[0][''])
        if(amountTotal >= loanDeatils[0]['total_loan']):
            status = 'completed'
            updateLoanDetails = """
                                    UPDATE loan_application SET amount_paid = %s, status  = %s WHERE loan_id = %s """
            slph = (amountTotal,status,loan_id)
            # amountPaid = amountPaid + each['amount_to_pay']
            db.update(updateLoanDetails,slph)
            
        # return loanRepayment

     except Exception as e:
        print(f"Error fetching loan types: {e}")
        return []
def searchUsers(staff_id,coop_id):
    try:
        db = current_app.db
     
        # add to the users wallet
        getLoanData = """
                SELECT * FROM member_cooperatives where cooperative_id = %s  and user_id = %s
                        """
        getParamsUser = (coop_id,staff_id,)


        checkUser = db.read(getLoanData,getParamsUser)
        # return checkUser
        if checkUser:
            staff = checkUser[0]['user_id']
            # return staff
            getUserData = """
                SELECT * FROM cooperative_members where staff_id = %s
                        """
            getParams = (staff,)


            users = db.read(getUserData,getParams)

            return users

        return []
    except Exception as e:
        print(f"Error fetching loan types: {e}")
        return []
    
def fetch_announcement(coop_id):
    try:
        db = current_app.db
     
        # add to the users wallet
        getLoanData = """
                SELECT * FROM announcement where coop_id = %s  and status = 'active'
                        """
        getParamsUser = (coop_id,)
        loanRepayment = db.read(getLoanData,getParamsUser)
        return loanRepayment
    except Exception as e:
        print(f"Error fetching loan types: {e}")
        return []
def getUserCooptives(staff_id):
    try:
        db = current_app.db
     
        # add to the users wallet
        getCoops = """
                SELECT * FROM member_cooperatives where user_id = %s 
                        """
        getParamscoops = (staff_id,)
        getCoops = db.read(getCoops,getParamscoops)

        response = []
        for each in getCoops:
             print(each)
             getCoopData = """
                SELECT * FROM cooperative WHERE coop_id = %s 
                        """
             getParamscoopsdata = (each['cooperative_id'],)
             coopsData = db.read(getCoopData,getParamscoopsdata)
             response.append({"coopData":coopsData[0],"subscription":each})

        print (len(response))    
        return response
            


    
        # string_list = IDS.strip(',').split(',')
        # placeholders = ', '.join(['%s'] * len(string_list))
        # query = f"SELECT * FROM cooperative WHERE coop_id IN ({placeholders})"
        # # query = "SELECT id, fullname, email, phoneno, address, staff_id, dob, gender   FROM cooperative_members WHERE %s IN staff_id"
        # # print(query)
        # try:
        #     # par = (IDS,)
        #     members = db.read(query, string_list)
        #     return members
        # except Exception as e:
        #     print(f"Error fetching members: {e}")
        #     return {"error": "Error fetching members"}

        #     return loanRepayment
    except Exception as e:
        print(f"Error fetching loan types: {e}")
        return []
def subscribeMember(coop_id,staff_id,amount):
    try:
        db = current_app.db
        print(coop_id)
        updateQuery = """
                        UPDATE member_cooperatives SET membership_status = 'subscribed' WHERE user_id = %s and cooperative_id = %s  
                    """
        paramsQuerys = (staff_id,coop_id,)

        db.update(updateQuery,paramsQuerys)

        createtransactions(coop_id,staff_id,amount,"credit","user-coop","subscription")

        return "done"
    except Exception as e:

        return []
def savingsPlan(staff_id,savings_id,frequency,amount,coop_id,title):
    try:
        db = current_app.db
        query = """
                INSERT INTO savingsplan (staff_id,savings_id,frequency,amount,coop_id,title) VALUES (%s,%s,%s,%s,%s,%s)
            """
        params = (staff_id,savings_id,frequency,amount,coop_id,title)
        db.create(query,params)

        return 0
    except Exception as e:
            print(e)
            return [] 

def getsavingsPlan(staff_id,coop_id):
    try:
        print(staff_id+" "+coop_id)
        db = current_app.db
        query = """
                SELECT * FROM savingsplan WHERE coop_id = %s and staff_id = %s
                """
        params = (coop_id,staff_id,)
        result = db.read(query,params)

        return result
    except Exception as e:
            print(e)
            return []
def getTransactions(coop_id,staff_id,type):
        try:
            db = current_app.db
            if(type=="all"):
                query = """
                    SELECT * FROM transactions WHERE coop_id = %s and staff_id = %s   

                                        """
                params = (coop_id,staff_id,)
                result = db.read(query,params)
                return result
            else:
                query = """
                    SELECT * FROM transactions WHERE coop_id = %s and staff_id = %s and type=%s  
                    """
                params = (coop_id,staff_id,type,)
                result = db.read(query,params)
                return result
        except Exception as e:
            return []

