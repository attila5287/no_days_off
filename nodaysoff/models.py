from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from nodaysoff import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# =============================
class Proday(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String (100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.png')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    tasks = db.relationship('Task', backref='manag5r', lazy=True)
    prodays = db.relationship('Proday', backref='planner', lazy=True)    
    urg_pts= db.Column(db.Integer, default=int(19)) 
    imp_pts = db.Column(db.Integer, default=int(19))
    total_pts = db.Column(db.Integer, default=int(38))
    imp_perc = db.Column(db.Integer, default=int(50))    
    urg_perc = db.Column(db.Integer, default=int(50))
    avatar_mode = db.Column(db.String(20), nullable=False, default='')
    avatar_img =  db.Column(db.String(20), nullable=False, default='default00.png')
    

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

    def init_points(self):
        pass
    # init points: importance
        if self.imp_pts == None:
            self.imp_pts = 0
            db.session.commit()
        else:
            pass            
    # init points: urgency        
        if self.urg_pts == None:
            self.urg_pts = 0
            db.session.commit()
        else:
            pass
    # init points: total points        
        if self.total_pts == None:
            self.total_pts = 0
            db.session.commit()
        else:
            pass
        
    def init_percs(self):
        pass
        # init percentage of points if None
        if self.imp_perc == None:
            self.imp_perc = 50
            self.urg_perc ==50
            db.session.commit()
        else:
            pass            
        if self.urg_perc == None:
            self.imp_perc = 50
            self.urg_perc = 50
            db.session.commit()
        else:
            pass
        self.imp_perc =  int(
            round(float(self.imp_pts/(self.imp_pts + self.urg_pts)),2)*100
            )
        self.urg_perc =  int(100 - self.imp_perc)
        db.session.commit()
    
    def update_percs(self):
        pass
        self.imp_perc =  int(
            round(float(self.imp_pts/(self.imp_pts + self.urg_pts)),2)*100
            )
        self.urg_perc =  int(100 - self.imp_perc)
        db.session.commit()
    
        
    def init_avatar(self):
        pass
        if self.avatar_img == None:
            self.avatar_img = 'avatar10.png'
            db.session.commit()
        else:
            pass
        
    def init_avatarmode(self):
        pass
        if self.avatar_mode == None:
            pass
            self.avatar_mode = ''
        else:
            pass
        

    def update_avatar(self):
        pass
        img_key = int(self.urg_perc)
        
        responsive = 53
        resp_n_act = 51
        act_n_resp = 49
        pro_active = 48
        
        if responsive < img_key :
            pass
            img_key = 'responsive'
        elif resp_n_act < img_key:
            pass
            img_key = 'resp_n_act'
        elif act_n_resp < img_key:
            pass
            img_key = 'resp_n_act'
        else:
            img_key = 'pro_active'

        img_dict = {
            'responsive': '11', 
            'resp_n_act': '10', 
            'act_n_resp': '01', 
            'pro_active': '00' 
        }
        
        print('img key for avatar...')
        print(img_key)

        updated_avatar = img_dict[img_key]

        print('upd avatar key...')
        print(updated_avatar)
        
        if updated_avatar:
            self.avatar_img = 'avatar' + img_dict[img_key] + '.png'
            print('assigned avatar...')
            print(self.avatar_img)
            db.session.commit()
        else:
            self.avatar_img = 'avatar10.png'
            print(self.avatar_img)
            db.session.commit()
            
    
    def gain_points(self, task_urg_pts=29, task_imp_pts=29):
        pass
        self.imp_pts+=task_imp_pts
        self.total_pts+=task_imp_pts
        self.urg_pts+=task_urg_pts
        self.total_pts+=task_urg_pts
        
        
    def lose_points(self, task_urg_pts=29, task_imp_pts=29):
        pass
        self.imp_pts-=task_imp_pts
        self.total_pts-=task_imp_pts
        self.urg_pts-=task_urg_pts  
        self.total_pts-=task_urg_pts      
        
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String (100), nullable=False)
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
