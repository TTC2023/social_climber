from flask_app.config.mysqlconnection import connectToMySQL

class Like:
    def __init__(self,data):
        self.id = data['id']
        self.post_id = data['post_id']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO likes (post_id,user_id) VALUES(%(post_id)s,%(user_id)s)"
        return connectToMySQL('social_climber').query_db(query,data)
