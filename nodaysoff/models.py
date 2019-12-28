from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from nodaysoff import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.png')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    tasks = db.relationship('Task', backref='manag5r', lazy=True)


    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    content = db.Column(db.Text)
    done = db.Column(db.Boolean, default=False)
    is_urgent = db.Column(db.Text, default='n')
    is_important = db.Column(db.Text, default='n')
    matrix_zone = db.Column(db.Text, default='00')
    border_style = db.Column(db.Text, default='info')
    urg_points= db.Column(db.Integer, default=int(36)) 
    imp_points = db.Column(db.Integer, default=int(36))
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
 
    def add_matrix_zone(self):
        pass
        self.matrix_zone = str(self.is_urgent) + str(self.is_important)
    
    def add_task_border(self):
        pass
        style_dict = {'11' : 'danger', '10' : 'warning', '01' : 'primary', '00' : 'info'}
        self.border_style = style_dict[self.matrix_zone]
    
    def add_urgency_points(self):
        pass
        urgency_point_dict = {
            '11' : '96',
            '10' : '72',
            '01' : '48',
            '00' : '36',
        }
        self.urg_points = int(urgency_point_dict[self.matrix_zone])

    def add_importance_points(self):
        pass
        importance_point_dict = {
            '11' : '96',
            '10' : '48',
            '01' : '72',
            '00' : '36',
        }
        self.imp_points = int(importance_point_dict[self.matrix_zone])        

    def __repr__(self):
        return '<Task %s>' % self.title
# ===================================
