from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="lifeiseasy#123",
    database="LoanEase"
)
cursor = db.cursor(dictionary=True)

# API Endpoint: Loan Eligibility Check
@app.route("/check_eligibility", methods=["POST"])
def check_eligibility():
    data = request.json
    loan_amount = data["loan_amount"]
    income = data["income"]
    credit_score = data["credit_score"]
    employment_type = data["employment_type"]

    # SQL Query to find matching loans
    query = """
    SELECT * FROM Loans 
    WHERE min_loan_amount <= %s 
    AND max_loan_amount >= %s 
    AND min_credit_score <= %s 
    AND min_income <= %s 
    AND employment_type = %s
    """
    cursor.execute(query, (loan_amount, loan_amount, credit_score, income, employment_type))
    loans = cursor.fetchall()

    if not loans:
        return jsonify({"message": "No suitable loans found"}), 404

    return jsonify({"eligible_loans": loans})

# Run the API
if __name__ == "__main__":
    app.run(debug=True)
