from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user
from flask_app.models import service

class Service:
    db = "salon"
    def __init__(self,data):
        self.id = data["id"]
        self.cut = data["cut"]
        self.color = data["color"]
        self.description = data["description"]
        self.date = data["date"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user = None

    @staticmethod
    def is_valid(data):
        is_valid = True
        if len(data["cut"]) <= 0 or len(data["color"]) <= 0 or len(data["description"]) <= 0:
            is_valid = False
            flash("All fields Required.")
            return is_valid
        if len(data["cut"]) < 2:
            is_valid = False
            flash("Please type Yes or No.")
        if len(data["color"]) < 2:
            is_valid = False
            flash("Please type Yes or No.")
        if len(data["description"]) < 4:
            is_valid = False
            flash("Must provide a description")
        return is_valid

    @classmethod
    def get_all_services(cls):
        pass
    
    @classmethod
    def get_one_service(cls,data):
        pass
    
    @classmethod
    def create_new_service(cls,data):
        pass
    
    @classmethod
    def edit_existing_service(cls,data):
        pass
    
    @classmethod
    def delete_service(cls,data):
        pass
