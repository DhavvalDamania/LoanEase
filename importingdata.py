import pandas as pd
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="lifeiseasy#123",
    database="LoanEase"
)
cursor = conn.cursor()

# Read CSV file
df = pd.read_csv("sample_loan_data.csv")

# SQL query to insert data
sql = """INSERT INTO Loans (
    bank_name, loan_type, min_loan_amount, max_loan_amount, interest_rate, 
    tenure_years, processing_fee, prepayment_penalty, min_credit_score, 
    min_income, employment_type, dti_ratio_limit, co_applicant_allowed
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

# Iterate over the DataFrame and insert data
for _, row in df.iterrows():
    cursor.execute(sql, (
        row["Bank Name"], row["Loan Type"], row["Min Loan Amount"], row["Max Loan Amount"],
        row["Interest Rate (%)"], row["Tenure (Years)"], row["Processing Fee (%)"],
        row["Prepayment Penalty"], row["Min Credit Score"], row["Min Income"],
        row["Employment Type"], row["DTI Ratio Limit"], row["Co-Applicant Allowed"]
    ))

# Commit and close connection
conn.commit()
cursor.close()
conn.close()

print("CSV imported successfully!")
