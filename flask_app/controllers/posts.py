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

@app.route('/process/edit/<int:id>', methods=['POST'])
def process_edit(id):
    if not Post.validate_post(request.form):
        return redirect(f'/edit/post/{id}')
    Post.make_post(request.form)
    return redirect('/dashboard')

@app.route('/edit/post/<int:id>')
def edit_post(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': id
    }
    user_id={
        'id': session['user_id']
    }
    return render_template('edit.html',post=Post.get_by_id(data))


@app.route('/delete/post/<int:id>')
def destroy(id):
    data={
        'id': id
    }
    Post.destroy(data)
    return redirect('/dashboard')