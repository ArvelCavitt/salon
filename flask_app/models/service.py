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
        query = "SELECT * FROM service JOIN user ON service.user_id = user.id;"
        results = connectToMySQL(cls.db).query_db(query)
        print("results", results)
        if len(results) == 0:
            return []
        else:
            service = []
            for row in results
            service_obj = cls(row)
            user_dictionary = {
                "id": row['user_id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "phone": row['phone'],
                "email": row['email'],
                "created_at": row['user.created_at'],
                "updated_at": row['user.updated_at']
            }
            user_obj = user.User(user_dictionary)
            service_obj.user = user_obj
            service.append(service_obj)
        print("service", service)
        return service
    
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
