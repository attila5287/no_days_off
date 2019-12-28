from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from nodaysoff.config import Config


db = SQLAlchemy()
# db.create_all()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from nodaysoff.users.routes import users
    from nodaysoff.posts.routes import posts
    from nodaysoff.tasks.routes import tasks
    from nodaysoff.main.routes import main
    from nodaysoff.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(tasks)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
