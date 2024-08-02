def straight_line_loan_schedule(principal, tenure_months, annual_interest_rate):
 
 
    interest_rate = annual_interest_rate / 100

 
    total_interest = principal * interest_rate * (tenure_months / 12)
    
    # Calculate monthly principal repayment
    monthly_principal_repayment = principal / tenure_months
    
    # Calculate monthly interest repayment
    monthly_interest_repayment = total_interest / tenure_months
    
    # Calculate monthly repayment (principal + interest)
    monthly_repayment = monthly_principal_repayment + monthly_interest_repayment
    
    # Generate the repayment schedule
    schedule = []
    remaining_principal = principal
    principalDisburesd = monthly_repayment * tenure_months
    for month in range(1, tenure_months + 2):
        # Deduct the monthly principal repayment from the remaining principal
        currentInterest = 0
        currentRepayment = 0
        if month == 1:
            principalDisburesd = principal
            currentInterest = 0
            currentRepayment = 0 
        else:
            principalDisburesd = 0.0
            currentInterest = monthly_interest_repayment
            currentRepayment = monthly_principal_repayment
        schedule.append({
            "month": month,
            "monthly_repayment": round((currentRepayment + currentInterest), 2),
            "monthly_principal_repayment": round(currentRepayment, 2),
            "monthly_interest_repayment": round(currentInterest, 2),
            "remaining_principal": round(remaining_principal, 2),
            "amount_received": round(principalDisburesd,2),
        })
        remaining_principal -= monthly_principal_repayment
    return schedule

def straight_line_upfront_loan_schedule(principal, tenure_months, annual_interest_rate):
    monthlyRepayment = principal / tenure_months
    interest = principal * (annual_interest_rate/100)
    principalDisburesd = principal - interest

    # print(principalDisburesd)
   
    schedule = []
    
    # # Single payment of principal at the end
    # monthly_principal_repayment = 0.0
    remaining_principal =  principal 
    # # Monthly repayment is only interest for each month
    for month in range(1, tenure_months + 2):
        currentrepayment = 0
        currenttotalrepayment = 0
        if month == 1:
            principalDisburesd= principalDisburesd
            interest =  interest
            currentrepayment = 0
            currenttotalrepayment = interest
        else:
            principalDisburesd = 0
            interest = 0
            currentrepayment = monthlyRepayment
            currenttotalrepayment = monthlyRepayment
        schedule.append({
            "month": month,
            "monthly_repayment": round(currenttotalrepayment, 2),
            "monthly_principal_repayment": round(currentrepayment, 2),
            "monthly_interest_repayment": round(interest, 2),
            "remaining_principal": round(remaining_principal, 2),
            "amount_received": round(principalDisburesd,2)
        })
        remaining_principal = remaining_principal - monthlyRepayment
    return schedule

def reducingBalance_loan_schedule(principal, tenure_months, annual_interest_rate):
    monthlyRepayment = principal / tenure_months
    # interest = principal * (annual_interest_rate/100)
    principalDisburesd = principal

    # print(principalDisburesd)
   
    schedule = []
 
    remaining_principal =  principal 
   
    for month in range(1, tenure_months + 2):
        currentrepayment = 0
        currenttotalrepayment = 0
        if month == 1:
            principalDisburesd= principalDisburesd
            interest =  0
            currentrepayment = 0
            currenttotalrepayment = interest
        else:
            principalDisburesd = 0
            # print(remaining_principal)
            interest = remaining_principal * (annual_interest_rate/100)
            currentrepayment = monthlyRepayment
            currenttotalrepayment = monthlyRepayment
            remaining_principal = remaining_principal - monthlyRepayment
        schedule.append({
            "month": month,
            "monthly_repayment": round((currenttotalrepayment + interest), 2),
            "monthly_principal_repayment": round(currentrepayment, 2),
            "monthly_interest_repayment": round(interest, 2),
            "remaining_principal": round(remaining_principal, 2),
            "amount_received": round(principalDisburesd,2)
        })
        
    return schedule

 
# principal = 100000
# tenure_months = 12
# annual_interest_rate = 10

# loan_schedule = reducingBalance_loan_schedule(principal, tenure_months, annual_interest_rate)
# for month in loan_schedule:
#     print(f"Month {month['month']}: Repayment: {month['monthly_repayment']}, Principal: {month['monthly_principal_repayment']}, Interest: {month['monthly_interest_repayment']}, Remaining Principal: {month['remaining_principal']}")