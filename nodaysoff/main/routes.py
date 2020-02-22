from flask import render_template, request, Blueprint
from nodaysoff.models import Post

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/about")
def about():
    pass
    return render_template(
        'about.html',
         title='About'
    )

@main.route("/aboutdev")
def aboutdev():
    return render_template(
        template_name_or_list='aboutdev.html',
        title='about developer'
    )

@main.route("/home")
def home():
    pass
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)

