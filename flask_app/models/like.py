from flask_app.config.mysqlconnection import connectToMySQL

class Like:
    def __init__(self,data):
        self.id = data['id']
        self.post_id = data['post_id']
        self.user_id = data['user_id']
        self.status = data['status']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_likes(cls):
        query = "SELECT * FROM likes;"
        results = connectToMySQL('social_climber').query_db(query)
        likes = []
        for l in results:
            likes.append( cls(l) )
        return likes

    @classmethod
    def save(cls,data):
        query = "INSERT INTO likes (post_id,user_id,status) VALUES(%(post_id)s,%(user_id)s,%(status)s)"
        return connectToMySQL('social_climber').query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM likes WHERE likes.post_id = %(post_id)s and likes.user_id = %(user_id)s"
        print("deleted........")
        return connectToMySQL('social_climber').query_db(query,data)
