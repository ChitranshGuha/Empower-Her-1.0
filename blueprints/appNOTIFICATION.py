import random
from flask import Blueprint, render_template, request, redirect, url_for, flash
import sqlite3

appNOTIFICATION_bp = Blueprint('notifications', __name__, template_folder='../templates')

# Database connection
def connect_db():
    return sqlite3.connect('feedbackNnotif.db')

# Function to initialize the database
def initialize_db():
    conn = connect_db()
    # cursor = conn.cursor()

    # with open('init_db.sql', 'r') as sql_file:
    #     sql_script = sql_file.read()
    #     cursor.executescript(sql_script)

    conn.commit()
    conn.close()

# Function to get a random notification from the database
def get_random_notification():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM notifications")
    notifications = cursor.fetchall()
    conn.close()

    if notifications:
        return random.choice(notifications)[1]  # message in the second column
    return None

# Home route
@appNOTIFICATION_bp.route('/')
def home():
    notification = get_random_notification()
    return render_template('home.html', notification=notification)

# Feedback form submission
@appNOTIFICATION_bp.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO feedback (name, email, message) VALUES (?, ?, ?)", (name, email, message))
        conn.commit()
        conn.close()

        flash("Thank you for your feedback!", "success")
        return redirect(url_for('notifications.home'))

    return render_template('feedback.html')

# Notifications route
@appNOTIFICATION_bp.route('/notifications')
def notifications():
    conn = connect_db()
    cursor = conn.cursor()
    
    # Fetch the last 10 notifications, assuming notifications have an 'id' or 'timestamp' for ordering
    cursor.execute("SELECT * FROM notifications ORDER BY id DESC LIMIT 10")  # Adjust 'id' as needed
    notifications = cursor.fetchall()
    conn.close()

    return render_template('notifications.html', notifications=notifications)

# Initialize the database if necessary
initialize_db()
