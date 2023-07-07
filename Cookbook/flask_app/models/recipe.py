from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


import re	
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class Recipe:
    DB="Cookbook"


    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.DateCook_Made = data['DateCook_Made']
        self.Under_30_minutes = data['Under_30_minutes']
        self.Users_id = data['Users_id']