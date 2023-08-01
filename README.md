# sync-signup-login
This is a registration application for users to sign up and login. built with Flask and SQLAlchemy.

## Description

The User Registration Application is a web-based application that allows users to register and login to the system. It provides a secure and user-friendly interface for managing user accounts.

## Features

- User registration: Users can create an account by providing their name, email, and password.
- User login: Registered users can login to access their account.
- Password encryption: User passwords are securely encrypted using bcrypt for enhanced security.
- Data storage: User information is stored in a relational database using SQLAlchemy.
- Error handling: Appropriate error messages are displayed to users for invalid input or unauthorized access.

## Installation

1. Clone the repository:
   ```https://github.com/mateuscavalcant/sync-signup-login```

3. Install the required dependencies:
```sh
pip install flask
```
```sh
pip install python-dotenv
```
```sh
pip install mysql-connector-python
```
3. Set up the database:
```mysql+mysqlconnector://user:password@host/your_database```


4. Run ```main.py``` to start the application


## Usage

1. Access the application in your web browser at `http://localhost:5000`.
2. Register a new user account by providing the required information.
3. Log in using your registered email and password.
4. Explore the features and manage your user account.
