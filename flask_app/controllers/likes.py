from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.like import Like
from flask_app.models.post import Post

@app.route('/like/<int:post_id>/<int:user_id>', methods=['POST'])
def process_like(post_id, user_id):
    data = {
        "post_id": post_id,
        "user_id": user_id,
    }
    Like.save(data)
    return redirect('/dashboard')


@app.route('/unlike/<int:post_id>/<int:user_id>', methods=['POST'])
def destroy_like(post_id, user_id):
    data = {
        "post_id": post_id,
        "user_id": user_id,
    }
    Like.destroy(data)
    return redirect('/dashboard')