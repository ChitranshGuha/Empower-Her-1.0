from flask import Flask, render_template, send_from_directory, current_app
from flask_socketio import SocketIO
from blueprints.appNOTIFICATION import appNOTIFICATION_bp
from blueprints.userlogin import userlogin_bp, init_db
from blueprints.personalize import personalize_bp
from blueprints.database import db  # Import db from database.py
from blueprints.app import jobs_bp
from blueprints.job_posting import job_posting_bp, init_job_table
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Initialize SocketIO
socketio = SocketIO(app)

# Configuration settings
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Max file size 16MB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///profiles.db'  # SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable track modifications

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///job_portal.db'  # SQLite database for job postings
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable track modifications

# Initialize the database
db.init_app(app)  # Initialize SQLAlchemy with the app

# Create the upload folder if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Initialize other databases
init_db(app)  # From userlogin.py
init_job_table(app)

# Create the database tables
with app.app_context():
    db.create_all()

# Register the blueprints
app.register_blueprint(userlogin_bp)
app.register_blueprint(appNOTIFICATION_bp)
app.register_blueprint(personalize_bp, url_prefix='/personalize')
app.register_blueprint(jobs_bp)  # Register jobs blueprint
app.register_blueprint(job_posting_bp)

@app.route('/uploads/<filename>')
def uploads(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)

@app.route('/email-sent')
def email_sent():
    return render_template('email_sent.html')  # Email confirmation page

@app.route('/index1')
def index1():
    return render_template('index1.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/overview')
def overview():
    return render_template('overview.html')

@app.route('/homepage1')
def homepage1():
    return render_template('homepage1.html')

@app.route('/homepage2')
def homepage2():
    return render_template('homepage2.html')

@app.route('/chatbox')
def chatbox():
    return render_template('chatbox.html')

@app.route('/agent')
def agent():
    return render_template('agent.html')

# Start the application
if __name__ == '__main__':
    socketio.run(app, debug=True)
