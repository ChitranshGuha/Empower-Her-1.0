# Empower-Her 1.0

Empower-Her 1.0 is a platform designed to support and empower women, providing them with tools and resources to help them advance in their careers, build skills, and connect with opportunities. This repository contains the code and resources for the Empower-Her web application.

## Table of Contents

* [About](#about)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Installation](#installation)
* [Usage](#usage)
* [Database Structure](#database-structure)
* [License](#license)
* [Contributing](#contributing)

## About

Empower-Her is an initiative to support women's career growth by providing a platform where they can access job listings, mentorship, and feedback from peers. The web app also allows users to register, log in, and interact with others in a secure, supportive environment.

This project is developed using Python, HTML, CSS, and JavaScript.

## Features

* **User Registration & Login**: Users can register and log in to their accounts securely.
* **Job Portal**: A section where users can find job listings relevant to their interests and skills.
* **Feedback System**: Allows users to provide and receive feedback.
* **Notifications**: Real-time notifications to keep users updated.

## Technologies Used

* **Frontend**:

  * HTML
  * CSS
  * JavaScript
* **Backend**:

  * Python
* **Database**:

  * SQLite (for storing user data, job listings, feedback, etc.)

## Installation

Follow the steps below to set up the project on your local machine:

1. Clone the repository:

   ```bash
   git clone https://github.com/ChitranshGuha/Empower-Her-1.0.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Empower-Her-1.0
   ```

3. Install the required dependencies:

   * If you're using Python, make sure you have the necessary libraries installed. You can do so by running:

     ```bash
     pip install -r requirements.txt
     ```

4. Set up the database:

   * The project uses SQLite for data storage. You can initialize the database by running the relevant SQL script (`test.sql` or other `.db` files).

## Usage

1. Start the web application:

   * If using a Flask or Django app, run the following command:

     ```bash
     python main.py
     ```
   * This will start the development server.

2. Open your browser and go to:

   ```text
   http://127.0.0.1:5000
   ```

3. Explore the features like user registration, job listings, feedback system, and notifications.

## Database Structure

The project uses SQLite databases to manage different data sections. Here are the key database files:

* `loginregister.db`: Stores user information (e.g., username, password).
* `job_portal.db`: Stores job listings.
* `feedbackNnotif.db`: Stores feedback and notifications.
* `test.sql`: Contains SQL setup for initializing the databases.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

We welcome contributions to improve Empower-Her. If you'd like to contribute, please fork the repository, create a new branch, and submit a pull request.
