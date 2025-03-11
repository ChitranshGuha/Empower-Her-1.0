import re
import sqlite3
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .database import db

userlogin_bp = Blueprint('userlogin', __name__, template_folder='templates')

# Function to create a connection to the database
def get_db_connection():
    conn = sqlite3.connect('loginregister.db')
    conn.row_factory = sqlite3.Row
    return conn

# Initialize the database and create users table
def init_db(app):
    with app.app_context():
        conn = get_db_connection()
        conn.execute('''CREATE TABLE IF NOT EXISTS users
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                         username TEXT NOT NULL UNIQUE,
                         email TEXT NOT NULL UNIQUE,
                         password TEXT NOT NULL)''')
        conn.commit()
        conn.close()


# User model
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

@userlogin_bp.route('/')
def home():
    return render_template('index.html')

@userlogin_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Validate username
        if not re.match("^[a-zA-Z0-9]{3,20}$", username):
            flash('Username must be 3-20 characters long and can only contain letters and numbers.', 'danger')
            return redirect(url_for('userlogin.register'))

        # Validate email
        if not re.match(r"^[^@]+@[^@]+\.[^@]+$", email) or len(email) > 254:
            flash('Invalid email address. Email must be less than 255 characters.', 'danger')
            return redirect(url_for('userlogin.register'))

        # Validate password
        if len(password) < 12:
            flash('Password must be at least 12 characters long.', 'danger')
            return redirect(url_for('userlogin.register'))
        if password != confirm_password:
            flash('Passwords do not match.', 'danger')
            return redirect(url_for('userlogin.register'))

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        # Add user to the database
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        try:
            db.session.commit()
            flash('Registration successful! Welcome!', 'success')
            return redirect(url_for('index1'))
        except Exception as e:
            db.session.rollback()
            flash('Username or email already exists. Please choose a different one.', 'danger')
            return redirect(url_for('userlogin.register'))

    return render_template('register.html')

@userlogin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash('Login successful!', 'success')
            return redirect(url_for('homepage2'))
        else:
            flash('Invalid username or password.', 'danger')
            return redirect(url_for('userlogin.login'))

    return render_template('login.html')

@userlogin_bp.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please log in to access this page.', 'warning')
        return redirect(url_for('userlogin.login'))

    return f'Hello, {session["username"]}! Welcome to your dashboard.'

@userlogin_bp.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('userlogin.login'))
