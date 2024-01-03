from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
import re

bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db= "salon"
    def __init__():
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def new_user(cls,data):
        query = "INSERT INTO user (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_id(cls,data):
        query = "SELECT * FROM user WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if results == ():
            return False
        else:
            return results[0]

    @classmethod
    def get_email(cls,data):
        query = "SELECT * FROM user WHERE email = %(email)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if results == ():
            return False
        else:
            return results[0]
    
    @staticmethod
    def validate_register(user):
        is_Valid = True
        query = "SELECT * FROM user WHERE email = %(email)s;"
        results = connectToMySQL(User.db).query_db(query, user)
        if len(results) >= 1:
            flash("Email already exists","register")
            is_Valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email","register")
            is_Valid = False
        if len(user['first_name']) < 3:
            flash("First name must contain at least three characters","register")
            is_Valid = False
        if len(user['last_name']) < 3:
            flash("Last name must contain at least three characters","register")
            is_Valid = False
        if len(user['password']) < 8:
            flash("Password must contain at least eight characters","register")
            is_Valid = False
        if user['password'] != user['confirm_password']:
            flash("Passwords do not match","register")
            is_Valid = False
        return is_Valid
    
    @staticmethod
    def validate_login(user_exist, user_login_data):
        is_Valid = True
        if not user_exist:
            flash("Invalid login credentials","login")
            is_Valid = False
        elif not bcrypt.check_password_hash(user_exist['password'], user_login_data['password']):
            flash("Invalid login credentials","login")
            is_Valid = False
        return is_Valid