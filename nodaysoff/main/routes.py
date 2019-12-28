from flask import render_template, request, Blueprint
from nodaysoff.models import Post

main = Blueprint('main', __name__)

# Drops all records, need to register again:DONT USE UNLESS NEW DB-MODEL 
# db.drop_all()
# Creates all tables, required if a new db-model to be tested
from flask import g 

@main.route("/")
@main.route("/home")
def home():
    pass

    if Post.query.first() == None:
        pass
        permanent_post = Post(
            title = 'Page Moved',
            content = 'use Wall for all Home features',
            author = current_user,
        )
        posts = [
            permanent_post
        ]
    else:
        pass
        page = request.args.get('page', 1, type=int)
        posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    
    
    return render_template('home.html', posts=posts)

@main.route("/about")
def about():
    return render_template('about.html', title='About')
