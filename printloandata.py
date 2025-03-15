from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'lifeiseasy#123',
    'database': 'Loanease'
}

def get_loans():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM loans")
    loans = cursor.fetchall()
    cursor.close()
    connection.close()
    return loans

@app.route('/')
def index():
    loans = get_loans()
    return render_template('loans.html', loans=loans)

if __name__ == '__main__':
    app.run(debug=True)