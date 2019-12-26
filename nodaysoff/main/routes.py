from flask import render_template, request, Blueprint
from nodaysoff.models import Post

main = Blueprint('main', __name__)

# Drops all records, need to register again:DONT USE UNLESS NEW DB-MODEL 
# db.drop_all()
# Creates all tables, required if a new db-model to be tested
from flask import g 


bootstrap_colors_list = [
    "cola", 
    "temptress", 
    "blackberry", 
    "ripe-plum", 
    "paua", 
    "prussian-blue", 
    "astronaut-blue", 
    "crusoe", 
    "la-palma", 
    "zest", 
    "thunderbird", 
    "red-violet", 
    "purple-heart", 
    "fun-blue", 
    "havelock-blue", 
    "persian-green", 
    "lima", 
    "galliano", 
    "deep-blush", 
    "nutmeg", 
    "milano-red", 
    "lipstick", 
    "purple", 
    "blue-gem", 
    "science-blue", 
    "teal", 
    "laurel", 
    "malachite", 
    "tree-poppy", 
    "scarlet", 
    "rose", 
    "heliotrope", 
    "dodger-blue", 
    "robins-egg-blue", 
    "pistachio", 
    "corn", 
    "hot-pink", 
    "black", 
    "white", 
    "lime", 
    "green", 
    "emerald", 
    "blue", 
    "teal", 
    "cyan", 
    "cobalt", 
    "indigo", 
    "violet", 
    "pink", 
    "magenta", 
    "crimson", 
    "red", 
    "orange", 
    "amber", 
    "yellow", 
    "brown", 
    "olive", 
    "steel", 
    "mauve", 
    "taupe", 
    "dark", 
    ]

@main.route("/")
@main.route("/home")
def home():
    pass
    g.bootstrap_colors_list = bootstrap_colors_list.copy()
    ColorList = bootstrap_colors_list.copy()
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts, BootstrapColorList = ColorList)

@main.route("/about")
def about():
    return render_template('about.html', title='About')
