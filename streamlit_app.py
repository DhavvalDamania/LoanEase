import streamlit as st
import requests

st.title("Loan Eligibility Checker")

loan_amount = st.number_input("Enter Loan Amount", min_value=0)
income = st.number_input("Enter Income", min_value=0)
credit_score = st.number_input("Enter Credit Score", min_value=0)
employment_type = st.selectbox("Employment Type", ["Salaried", "Self-Employed"])

if st.button("Check Eligibility"):
    response = requests.get("http://127.0.0.1:5000/get_loans", params={
        "loan_amount": loan_amount,
        "income": income,
        "credit_score": credit_score,
        "employment_type": employment_type
    })
    loans = response.json()
    
    if loans:
        st.write("Eligible Loans:")
        st.table(loans)
    else:
        st.write("No eligible loans found.")

