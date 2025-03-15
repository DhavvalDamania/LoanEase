import pandas as pd
import numpy as np

# Function to generate random loan data
def generate_loan_data(num_entries):
    banks = ["Bank of America", "Chase", "Wells Fargo", "Citibank", "Capital One", "US Bank", "TD Bank", "PNC Bank", "SunTrust", "Regions Bank"]
    loan_types = ["Home Loan", "Auto Loan", "Personal Loan", "Student Loan", "Business Loan"]
    employment_types = ["Salaried", "Self-Employed", "Student", "Business Owner"]
    prepayment_penalties = ["Yes", "No"]
    co_applicant_allowed = ["Yes", "No"]
    
    data = []
    for _ in range(num_entries):
        bank_name = np.random.choice(banks)
        loan_type = np.random.choice(loan_types)
        min_loan_amount = np.random.randint(1000, 100000)
        max_loan_amount = np.random.randint(min_loan_amount, 1000000)
        interest_rate = round(np.random.uniform(3.0, 15.0), 2)
        tenure = np.random.randint(1, 30)
        processing_fee = round(np.random.uniform(0.5, 3.0), 2)
        prepayment_penalty = np.random.choice(prepayment_penalties)
        min_credit_score = np.random.randint(600, 750)
        min_income = np.random.randint(20000, 100000)
        employment_type = np.random.choice(employment_types)
        dti_ratio_limit = np.random.randint(30, 60)
        co_applicant = np.random.choice(co_applicant_allowed)
        
        data.append({
            "Bank Name": bank_name,
            "Loan Type": loan_type,
            "Min Loan Amount": min_loan_amount,
            "Max Loan Amount": max_loan_amount,
            "Interest Rate (%)": interest_rate,
            "Tenure (Years)": tenure,
            "Processing Fee (%)": processing_fee,
            "Prepayment Penalty": prepayment_penalty,
            "Min Credit Score": min_credit_score,
            "Min Income": min_income,
            "Employment Type": employment_type,
            "DTI Ratio Limit": dti_ratio_limit,
            "Co-Applicant Allowed": co_applicant
        })
    
    return data

# Original data
original_data = [
    {"Bank Name": "Bank of America", "Loan Type": "Home Loan", "Min Loan Amount": 50000, "Max Loan Amount": 500000, "Interest Rate (%)": 6.5, 
     "Tenure (Years)": 30, "Processing Fee (%)": 1.2, "Prepayment Penalty": "No", "Min Credit Score": 700, "Min Income": 50000, "Employment Type": "Salaried", 
     "DTI Ratio Limit": 40, "Co-Applicant Allowed": "Yes"},
    
    {"Bank Name": "Chase", "Loan Type": "Auto Loan", "Min Loan Amount": 10000, "Max Loan Amount": 80000, "Interest Rate (%)": 4.5, 
     "Tenure (Years)": 7, "Processing Fee (%)": 0.5, "Prepayment Penalty": "No", "Min Credit Score": 650, "Min Income": 30000, "Employment Type": "Salaried", 
     "DTI Ratio Limit": 45, "Co-Applicant Allowed": "No"},
    
    {"Bank Name": "Wells Fargo", "Loan Type": "Personal Loan", "Min Loan Amount": 5000, "Max Loan Amount": 50000, "Interest Rate (%)": 10.0, 
     "Tenure (Years)": 5, "Processing Fee (%)": 2.0, "Prepayment Penalty": "No", "Min Credit Score": 680, "Min Income": 25000, "Employment Type": "Self-Employed", 
     "DTI Ratio Limit": 50, "Co-Applicant Allowed": "Yes"},
    
    {"Bank Name": "Citibank", "Loan Type": "Student Loan", "Min Loan Amount": 2000, "Max Loan Amount": 100000, "Interest Rate (%)": 5.0, 
     "Tenure (Years)": 10, "Processing Fee (%)": 1.5, "Prepayment Penalty": "No", "Min Credit Score": 620, "Min Income": 20000, "Employment Type": "Student", 
     "DTI Ratio Limit": 55, "Co-Applicant Allowed": "Yes"},
    
    {"Bank Name": "Capital One", "Loan Type": "Business Loan", "Min Loan Amount": 25000, "Max Loan Amount": 1000000, "Interest Rate (%)": 8.5, 
     "Tenure (Years)": 20, "Processing Fee (%)": 1.8, "Prepayment Penalty": "Yes", "Min Credit Score": 720, "Min Income": 75000, "Employment Type": "Business Owner", 
     "DTI Ratio Limit": 35, "Co-Applicant Allowed": "No"}
]

# Generate additional 50 entries
additional_data = generate_loan_data(500)

# Combine original and additional data
loan_data = pd.DataFrame(original_data + additional_data)

# Save to CSV file
loan_data.to_csv("sample_loan_data.csv", index=False)
print("CSV file 'sample_loan_data.csv' has been created successfully!")