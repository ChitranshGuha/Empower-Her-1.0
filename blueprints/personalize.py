from flask import Blueprint, request, jsonify, current_app
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
import logging
from flask_sqlalchemy import SQLAlchemy
from blueprints.database import db

# Create a blueprint
personalize_bp = Blueprint('personalize', __name__,template_folder='templates')
CORS(personalize_bp)

# Initialize the database
# db = SQLAlchemy()

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    contact_no = db.Column(db.String(15), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    job_preferences = db.Column(db.Text, nullable=False)
    working_hours = db.Column(db.String(50), nullable=False)
    bio = db.Column(db.Text, nullable=False)
    profile_picture = db.Column(db.String(200), nullable=False)
    id_proof = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Profile {self.name}>'



# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}

# In-memory storage for profiles
profiles = []

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@personalize_bp.route('/')
def home():
    return jsonify({'message': 'Welcome to the profile upload API! Use /upload-profile to upload your profile.'})

@personalize_bp.route('/upload-profile', methods=['POST'])
def upload_profile():
    try:
        upload_folder = current_app.config['UPLOAD_FOLDER']
        
        name = request.form.get('name')
        age = request.form.get('age')
        contact_no = request.form.get('contact_no')
        location = request.form.get('location')
        job_preferences = request.form.get('job_preferences')
        working_hours = request.form.get('working_hours')
        bio = request.form.get('bio')

        profile_picture = request.files.get('profile_picture')
        id_proof = request.files.get('id_proof')

        if not profile_picture or not id_proof:
            return jsonify({'error': 'Both profile picture and ID proof are required.'}), 400

        # Save profile picture as 'pfp.png'
        if profile_picture and allowed_file(profile_picture.filename):
            profile_picture_path = os.path.join(upload_folder, 'pfp.png')  # Save as pfp.png
            profile_picture.save(profile_picture_path)
        else:
            return jsonify({'error': 'Invalid profile picture format.'}), 400

        # Save ID proof as 'proof.png' (or adapt to the file type)
        if id_proof and allowed_file(id_proof.filename):
            id_proof_path = os.path.join(upload_folder, 'proof.png')  # Save as proof.png
            id_proof.save(id_proof_path)
        else:
            return jsonify({'error': 'Invalid ID proof format.'}), 400

        # Save to the database
        new_profile = Profile(
            name=name,
            age=age,
            contact_no=contact_no,
            location=location,
            job_preferences=job_preferences,
            working_hours=working_hours,
            bio=bio,
            profile_picture='pfp.png',  # Save the filename in the database
            id_proof='proof.png'  # Save the filename in the database
        )
        db.session.add(new_profile)
        db.session.commit()

        return jsonify({'success': 'Profile successfully uploaded!'})

    except Exception as e:
        logging.error(f"Error uploading profile: {str(e)}")
        return jsonify({'error': str(e)}), 500

@personalize_bp.route('/profile-overview', methods=['GET'])
def profile_overview():
    profiles = Profile.query.all()
    return jsonify([{
        'name': profile.name,
        'age': profile.age,
        'contact_no': profile.contact_no,
        'location': profile.location,
        'job_preferences': profile.job_preferences,
        'working_hours': profile.working_hours,
        'bio': profile.bio,
        'profile_picture': profile.profile_picture,
        'id_proof': profile.id_proof
    } for profile in profiles])