from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.post import Post
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/create/post')
def create_post():
    return render_template('create.html')

@app.route('/process/post', methods=['POST'])
def process_post():
    if not Post.validate_post(request.form):
        return redirect('/create/post')
    Post.make_post(request.form)
    return redirect('/dashboard')