from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


import re	
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class User:
    DB="Cookbook"

    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.fullname=data['first_name'] + " " + data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']





    @staticmethod
    def validate_user(user):
        is_valid = True # we assume this is true
        query  = "SELECT * FROM users WHERE email = %(email)s";
        data = {"email":user['email']}
        results = connectToMySQL(User.DB).query_db(query, data)
        if len(results) >=1:
            flash("Email is already taken")
            is_valid = False
        if len(user['first_name']) < 2:
            flash("First Name must be at least 3 characters.","reg")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("last name must be at least 3 characters.","reg")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!","reg")
            is_valid = False
        if len(user['password']) < 9:
            flash("Invalid Password 8 characters needed.","reg")
            is_valid = False
        if len(user['confirm_password']) < 9:
            flash("password do not match.","reg")
            is_valid = False
        if(user['password']!=user['confirm_password']):
            flash("Passwords mismatchs","reg")
            is_valid = False
        return is_valid


    @classmethod
    def save(cls, data):
        query = """INSERT INTO users (first_name,last_name,password,email,created_at)
        VALUES (%(first_name)s,%(last_name)s,%(password)s,%(email)s,NOW());"""
        result = connectToMySQL(cls.DB).query_db(query,data)
        print('result>>>>>>>>>',result)
        return result


    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(cls.DB).query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])