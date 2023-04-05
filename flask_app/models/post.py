from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask_app.models.user import User
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash

class Post:
    def __init__(self,data):
        self.id = data['id']
        self.location = data['location']
        self.type = data['type']
        self.grade = data['grade']
        self.comment = data['comment']
        self.user_id = data['user_id']

    @classmethod
    def make_post(cls,data):
        query = "INSERT INTO posts (location, type, grade, comment, user_id) VALUES(%(location)s,%(type)s,%(grade)s,%(comment)s,%(user_id)s);"
        result = connectToMySQL('social_climber').query_db(query,data)
        return result

    @classmethod
    def get_all_posts(cls):
        query = "SELECT * FROM posts;"
        results = connectToMySQL('social_climber').query_db(query)
        posts = []
        for p in results:
            posts.append( cls(p) )
        return posts

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM posts WHERE id = %(id)s;"
        results = connectToMySQL('social_climber').query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE posts SET location=%(location)s,type=%(type)s,grade=%(grade)s,comment=%(comment)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('social_climber').query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM posts WHERE id = %(id)s"
        return connectToMySQL('social_climber').query_db(query,data)

    @staticmethod
    def validate_post(post):
        is_valid = True
        results = connectToMySQL('social_climber').query_db(post)
        if len(post['location']) < 3:
            flash("Location must be at least 3 characters","post")
            is_valid= False
        if len(post['grade']) < 2:
            flash("Grade is required","post")
            is_valid= False
        if len(post['comment']) < 8:
            flash("Comments must be 8 characters or longer","post")
            is_valid= False
        return is_valid