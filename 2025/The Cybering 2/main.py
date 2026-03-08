# main.py
from flask import Flask, jsonify, render_template, request
import mysql.connector
import os
import cryptography

app = Flask(__name__)

def get_db_connection():
    """Establishes a connection to the MySQL database."""
    try:
        conn = mysql.connector.connect(
            host=os.environ.get('MYSQL_HOST'),
            user=os.environ.get('MYSQL_USER'),
            password=os.environ.get('MYSQL_PASSWORD'),
            database=os.environ.get('MYSQL_DB')
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

@app.route('/')
def index():
    """Serves the main HTML page."""
    return render_template('index.html')

@app.route('/submit', methods=["post"])
def submit():

    username = request.form.get("username")
    password = request.form.get("password")

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "SELECT flag FROM users WHERE username = '"+username+"' AND password = '"+password + "' LIMIT 1;"
        print(sql)
        
        cursor.execute(sql)
        flag = cursor.fetchone()
    except Exception as e:
        print(e)
        flag = None

    if flag:
        actual_flag = flag[0]
    else:
        actual_flag = "Intake{NiceTrySucker}"

    conn.close()

    return render_template('dashboard.html', token=actual_flag)

@app.route('/book_tickets')
def book_tickets():
    return render_template('book-tickets.html')

@app.route('/api/status')
def status():
    """API endpoint to check the database connection status."""
    conn = get_db_connection()
    if conn:
        conn.close()
        return jsonify(database_status='connected')
    else:
        return jsonify(database_status='disconnected'), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)