from flask_app.config.mysqlconnection import connectToMySQL
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash

class User:
    def __init__(self,data):
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (username,email,password) VALUES(%(username)s,%(email)s,%(password)s)"
        return connectToMySQL('social_climber').query_db(query,data)

    @classmethod
    def get_user_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('social_climber').query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('social_climber').query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @staticmethod
    def validate_register(user):
        is_valid = True
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid Email","register")
            is_valid=False
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('social_climber').query_db(query,user)
        if len(results) != 0:
            flash("* Email already exists","register")
            is_valid=False
        if len(user['username']) < 3:
            flash("Username must be at least 3 characters","register")
            is_valid= False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters","register")
            is_valid= False
        if user['password'] != user['confirm']:
            flash("Passwords don't match","register")
        return is_valid