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
        likes = []
        results = connectToMySQL('social_climber').query_db(query)
        for row in results:
            likes.append(cls(row))
        return likes

    @classmethod
    def get_all_likes_by_user(cls,data):
        query = "SELECT likes.id, users.id as user_id, posts.id as post_id, likes.status, likes.created_at, likes.updated_at FROM likes JOIN users ON likes.user_id = %(id)s JOIN posts ON likes.post_id = posts.id;"
        results = connectToMySQL('social_climber').query_db(query,data)

        likes = []
        print(results)
        for row in results:
            data = {
                "id": row['id'],
                "user_id": row['user_id'],
                "post_id": row['post_id'],
                "status": row['status'],
                "created_at": row['created_at'],
                "updated_at": row['updated_at']
            }
            likes.append(cls(data))
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
