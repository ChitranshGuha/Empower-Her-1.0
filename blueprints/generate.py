'''import sqlite3
import random
import string

# Database connection
def get_db_connection():
    conn = sqlite3.connect('job_portal.db')  # SQLite database file
    return conn

# Create user and job tables if they do not exist
def create_tables(conn):
    # Create User Table
    conn.execute("""
        CREATE TABLE IF NOT EXISTS user (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            emailid TEXT UNIQUE,
            name TEXT,
            skill1 TEXT,
            skill2 TEXT,
            skill3 TEXT,
            password TEXT
        )
    """)
    
    # Create Job Tables
    job_types = [
        'housekeeper', 'homecook', 'beautician',
        'caretaker', 'hostel_cook', 'laundry',
        'nanny', 'playschool_teacher', 'shop_attendant'
    ]
    
    for job_type in job_types:
        conn.execute(f"""
            CREATE TABLE IF NOT EXISTS {job_type} (
                jobid INTEGER PRIMARY KEY AUTOINCREMENT,
                name_of_organization TEXT,
                phone_number TEXT,
                location TEXT,
                salary INTEGER
            )
        """)
    
    conn.commit()

# Generate random user data
def generate_user_data():
    users = []
    for i in range(10):  # Generate 10 random users
        emailid = f'user{i}@example.com'
        name = f'User_{i}'
        skill1 = random.choice(['cooking', 'cleaning', 'childcare', 'beauty', 'laundry'])
        skill2 = random.choice(['cooking', 'cleaning', 'childcare', 'beauty', 'laundry'])
        skill3 = random.choice(['cooking', 'cleaning', 'childcare', 'beauty', 'laundry'])
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))  # Random 8 character password
        users.append((emailid, name, skill1, skill2, skill3, password))
    return users

# Generate random job data
def generate_job_data():
    job_types = [
        'housekeeper', 'homecook', 'beautician',
        'caretaker', 'hostel_cook', 'laundry',
        'nanny', 'playschool_teacher', 'shop_attendant'
    ]
    organizations = [f'Org_{i}' for i in range(1, 11)]  # 10 different organizations
    phone_numbers = [f'12345678{i}' for i in range(10)]  # 10 different phone numbers
    locations = ['Location A', 'Location B', 'Location C']
    salaries = [20000, 25000, 30000, 35000, 40000]

    conn = get_db_connection()
    create_tables(conn)  # Create tables

    # Insert user data
    users = generate_user_data()
    conn.executemany("""
        INSERT INTO user (emailid, name, skill1, skill2, skill3, password)
        VALUES (?, ?, ?, ?, ?, ?)
    """, users)

    # Insert job data
    cur = conn.cursor()
    for job_type in job_types:
        for _ in range(5):  # Generate 5 entries for each job type
            name_of_organization = random.choice(organizations)
            phone_number = random.choice(phone_numbers)
            location = random.choice(locations)
            salary = random.choice(salaries)

            # Insert data into the respective job table
            cur.execute(f"""
                INSERT INTO {job_type} (name_of_organization, phone_number, location, salary)
                VALUES (?, ?, ?, ?)
            """, (name_of_organization, phone_number, location, salary))

    conn.commit()
    cur.close()
    conn.close()
    print("Temporary user and job data generated successfully.")

if __name__ == '__main__':
    generate_job_data()'''

import sqlite3
import random
import string

# Database connection
def get_db_connection():
    conn = sqlite3.connect('job_portal.db')  # SQLite database file
    return conn

# Create user and job tables if they do not exist
def create_tables(conn):
    # Drop tables if they exist
    conn.execute("DROP TABLE IF EXISTS user")
    job_types = [
        'housekeeper', 'homecook', 'beautician',
        'caretaker', 'hostel_cook', 'laundry',
        'nanny', 'playschool_teacher', 'shop_attendant'
    ]
    
    # Drop existing job tables to remove any old structures
    for job_type in job_types:
        conn.execute(f"DROP TABLE IF EXISTS {job_type}")

    # Create User Table
    conn.execute(""" 
        CREATE TABLE IF NOT EXISTS user (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            emailid TEXT UNIQUE,
            name TEXT,
            skill1 TEXT,
            skill2 TEXT,
            skill3 TEXT,
            password TEXT
        )
    """)

    # Create Job Tables with emailid column
    for job_type in job_types:
        conn.execute(f"""
            CREATE TABLE IF NOT EXISTS {job_type} (
                jobid INTEGER PRIMARY KEY AUTOINCREMENT,
                name_of_organization TEXT,
                phone_number TEXT,
                location TEXT,
                salary INTEGER,
                emailid TEXT  -- New column added
            )
        """)

    conn.commit()

# Generate random user data
def generate_user_data():
    users = []
    existing_emails = set()  # To track existing emails
    while len(users) < 20:  # Generate 20 random users
        emailid = f'user{random.randint(1, 10000)}@example.com'  # Use random number for uniqueness
        if emailid not in existing_emails:  # Check if email is unique
            existing_emails.add(emailid)
            name = f'User_{len(users)}'
            skill1 = random.choice(['cooking', 'cleaning', 'childcare', 'beauty', 'laundry'])
            skill2 = random.choice(['cooking', 'cleaning', 'childcare', 'beauty', 'laundry'])
            skill3 = random.choice(['cooking', 'cleaning', 'childcare', 'beauty', 'laundry'])
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))  # Random 8 character password
            users.append((emailid, name, skill1, skill2, skill3, password))
    return users

# Generate random job data
def generate_job_data():
    job_types = [
        'housekeeper', 'homecook', 'beautician',
        'caretaker', 'hostel_cook', 'laundry',
        'nanny', 'playschool_teacher', 'shop_attendant'
    ]
    organizations = [f'Org_{i}' for i in range(1, 21)]  # 20 different organizations
    phone_numbers = [f'12345678{i}' for i in range(20)]  # 20 different phone numbers
    locations = ['Indore', 'Bhopal', 'Dewas', 'Ujjain', 'Sagar']
    salaries = [20000, 25000, 30000, 35000, 40000]

    conn = get_db_connection()
    create_tables(conn)  # Create tables

    # Insert user data
    users = generate_user_data()
    conn.executemany(""" 
        INSERT INTO user (emailid, name, skill1, skill2, skill3, password)
        VALUES (?, ?, ?, ?, ?, ?)
    """, users)

    # Insert job data
    cur = conn.cursor()
    for job_type in job_types:
        for _ in range(5):  # Generate 5 entries for each job type
            name_of_organization = random.choice(organizations)
            phone_number = random.choice(phone_numbers)
            location = random.choice(locations)
            salary = random.choice(salaries)
            emailid = random.choice(users)[0]  # Randomly assign an existing user email to the job

            # Insert data into the respective job table
            cur.execute(f"""
                INSERT INTO {job_type} (name_of_organization, phone_number, location, salary, emailid)
                VALUES (?, ?, ?, ?, ?)
            """, (name_of_organization, phone_number, location, salary, emailid))

    conn.commit()
    cur.close()
    conn.close()
    print("Temporary user and job data generated successfully.")

if __name__ == '__main__':
    generate_job_data()
