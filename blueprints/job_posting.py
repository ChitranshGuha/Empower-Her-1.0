import sqlite3
from flask import Blueprint, render_template, request, redirect, url_for, flash

job_posting_bp = Blueprint('job_posting', __name__)

def get_db_connection():
    conn = sqlite3.connect('job_portal.db')
    conn.row_factory = sqlite3.Row
    return conn

@job_posting_bp.route('/job_form')
def job_form():
    return render_template('job_form.html')

@job_posting_bp.route('/submit_job', methods=['POST'])
def submit_job():
    job_type = request.form['job_type']
    name_of_organization = request.form['name_of_organization']
    phone_number = request.form['phone_number']
    location = request.form['location']
    salary = request.form['salary']
    emailid = request.form['emailid']

    try:
        insert_job_data(job_type, name_of_organization, phone_number, location, salary, emailid)
        return "Successfully added! <a href='/homepage2'>Back to Home</a>"
    except Exception as e:
        print(f"Error: {e}")  # Log the error to the console
        return f"An error occurred: {str(e)}"

def insert_job_data(job_type, name_of_organization, phone_number, location, salary, emailid):
    table_name = job_type  # Assuming job_type matches the table name
    
    sql = f"""
        INSERT INTO {table_name} (name_of_organization, phone_number, location, salary, emailid)
        VALUES (?, ?, ?, ?, ?)
    """
    
    with get_db_connection() as conn:
        conn.execute(sql, (name_of_organization, phone_number, location, salary, emailid))
        conn.commit()

def init_job_table(app):
    with app.app_context():
        # Create all tables as needed if not using SQLAlchemy
        pass  # You would handle this as needed
