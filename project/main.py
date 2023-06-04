from flask import Blueprint, render_template, current_app, redirect, url_for, abort
from werkzeug.utils import secure_filename
from .forms import PostForm
from .models import Post
import os
from . import db 
from sqlalchemy.exc import SQLAlchemyError

ALLOWED_EXTENSIONS  = {'png', 'jpg', 'jpeg'}
main = Blueprint('main', __name__)
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main.route('/')
def home():
    posts_list = Post.query.order_by(Post.created_at).all()

    return render_template('home.html', posts_list=posts_list)

@main.route('/create', methods=['POST', 'GET'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        username = form.data.get('username')
        email    = form.data.get('email')
        content  = form.data.get('content')
        image    = form.data.get('picture')
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            image.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            post = Post(username=username, email=email, content=content, picture=filename)
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('main.home'))
        return "we need an image dude!"
    return render_template('create.html', form=form)

@main.route('/delete/<post_id>')
def delete(post_id):
    post = Post.query.get_or_404(post_id)
    if post:
        image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], post.picture)
        if os.path.exists(image_path):
            try:
                os.remove(image_path)
                db.session.delete(post)  # Assuming you are using SQLAlchemy
                db.session.commit()  # Commit the changes to the database
                return redirect(url_for('main.home'))
            except SQLAlchemyError as e:
                # Handle the database error appropriately (e.g., log the error, display a message)
                return abort(500, "Failed to delete the post")

        db.session.delete(post)  # Assuming you are using SQLAlchemy
        db.session.commit()  # Commit the changes to the database
        return redirect(url_for('main.home'))

    return abort(404, "Post not found")
