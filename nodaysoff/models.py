from datetime import datetime
import random
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app, g
from nodaysoff import db, login_manager
from flask_login import UserMixin

list_of_quotes = [
    'Work harder on yourself than you do on your job  ',
    'The only way it gets better for you is when you get better. Better is not something you wish, it’s something you become  ',
    'For things to change, you have to change  ',
    'Don’t let your learning lead to knowledge. Let your learning lead to action  ',
    'Success is not to be pursued, it is to be attracted by the person you become  ',
    'Success is nothing more than a few simple disciplines practiced every day  ',
    'When you know what you want, and you want it bad enough, you will find a way to get it  ',
    'The few who do are the envy of the many who only watch  ',
    'Time is more valuable than money. You can get more money, but you cannot get more time  ',
    'Formal education will make you a living, self-education will make you a fortune  ',
    'You are the average of the five people you spend the most time with  ',
    'Life does not get better by chance, it gets better by change  ',
    'All leaders are readers  ',
    'Don’t shortchange yourself when it comes to investing in your own better future  ',
    'Start reading, and especially read the kinds of books that will help you unleash your inner potential  ',
    'What you become is far more important than what you get  ',
    'I used to blame everything outside of me for my lack of progress until I found that my problem was inside  ',
    'If you will be faithful to a few things, you will someday become the ruler over many things  ',
    'Poor people spend their money and save what’s left, rich people save their money and spend what’s left  ',
    'Take interest and even delight in doing the small things well  ',
    'Living life in style also means living a life of balance  ',
    'Few key things that make a difference, once identified, spend major time on these things  ',
    'Life is not just the passing of time. Life is the collection of experiences and their intensity  ',
    'You cannot change your destination overnight but you can change your direction overnight  ',
    'Successful people do what unsuccessful people are not willing to do  ',
    'Don’t wish it was easier, wish you were better. Don’t wish for less problems, wish for more skills. Don’t wish for less challenges, wish for more wisdom  ',
    'Be fascinated instead of frustrated  ',
    'Unless you change how you are, you will always have what you got  ',
    'Either you run the day or the day runs you  ',
    'You must take personal responsibility. You cannot change the circumstances, the seasons, or the wind, but you can change yourself. That is something you have charge of  ',
    'Learning is the beginning of wealth. Learning is the beginning of health. Learning is the beginning of spirituality. Searching and learning is where the miracle process all begins  ',
    'Take care of your body. It’s the only place you have to live  ',
    'Finding is reserved for those who search  ',
    'Motivation is what gets you started. Habit is what keeps you going  ',
    'Happiness is not something you postpone for the future; it is something you design for the present  ',
    'Let others lead small lives, but not you. Let others argue over small things, but not you. Let others cry over small hurts, but not you. Let others leave their future in someone else’s hands, but not you  ',
    'Learn how to be happy with what you have while you pursue all that you want  ',
    'Everyone must choose one of two pains: The pain of discipline or the pain of regret  ',
    'The more you care, the stronger you can be  ',
    'If you don’t sow, you don’t reap. You don’t even have a chance  ',
    'To solve any problem, here are three questions to ask yourself: First, what could I do? Second, what could I read? And third, who could I ask? ”  ',
    'A good objective of leadership is to help those who are doing poorly to do well and to help those who are doing well and to help those who are doing well to do even better  ',
    'You must be careful not to let your current appetites steal away any chance we might have for a future feast  ',
    'If you don’t design your own life plan, chances are you’ll fall into someone else’s plan, and guess what they have planned for you? Not much  ',
    'The major key to your better future is you  ',
    'If you are not willing to risk the usual you will have to settle for the ordinary  ',
    'The worst thing one can do is not to try, to be aware of what one wants and not give in to it, to spend years in silent hurt wondering if something could have materialized  ',
    'If you grow, everything grows for you  ',
    'For every disciplined effort, there is a multiple reward  ',
    'Discipline is the bridge between goals and accomplishment  ',
    'The stronger the why, the easier the how becomes  ',
    'We cannot move casually into a better future. We cannot casually pursue the goal we have set for ourselves. A goal that is casually pursued is not a goal, at best it is a wish, and wishes are little more than self-delusion  ',
    'Don’t spend major time on minor things  ',
    'Every day, stand guard at the door of your mind  ',
    'Excuses are the nails used to build a house of failure  ',
    'You have two choices: You can make a living, or you can design a life  ',
]
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(db.Model, UserMixin):
    'user with tasks, prodays, posts, collecting points per completion along with profile pic, hashed password etc. '
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.png')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    tasks = db.relationship('Task', backref='manag5r', lazy=True)
    prodays = db.relationship('Proday', backref='planner', lazy=True)
    urg_pts = db.Column(db.Integer, default=int(19))
    imp_pts = db.Column(db.Integer, default=int(19))
    total_pts = db.Column(db.Integer, default=int(38))
    imp_perc = db.Column(db.Integer, default=int(50))
    urg_perc = db.Column(db.Integer, default=int(50))
    avatar_mode = db.Column(db.String(20), nullable=False, default='')
    avatar_img = db.Column(db.String(20), nullable=False,
                           default='default00.png')

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
            self.imp_pts = 1
            db.session.commit()
        else:
            pass
        # init points: urgency
        if self.urg_pts == None:
            self.urg_pts = 1
            db.session.commit()
        else:
            pass
        # init points: total points
        if self.total_pts == None:
            self.total_pts = 2
            db.session.commit()
        else:
            pass

    def init_percs(self):
        pass
        # init percentage of points if None
        if self.imp_perc == None:
            self.imp_perc = 50
            self.urg_perc == 50
            db.session.commit()
        else:
            pass
        if self.urg_perc == None:
            self.imp_perc = 50
            self.urg_perc = 50
            db.session.commit()
        else:
            pass
        self.imp_perc = int(
            round(float(self.imp_pts/(self.imp_pts + self.urg_pts)), 2)*100
        )
        self.urg_perc = int(100 - self.imp_perc)
        db.session.commit()

    def update_percs(self):
        pass
        self.imp_perc = int(
            round(float(self.imp_pts/(self.imp_pts + self.urg_pts)), 2)*100
        )
        self.urg_perc = int(100 - self.imp_perc)
        db.session.commit()

    def gain_points(self, task_urg_pts=29, task_imp_pts=29):
        pass
        self.imp_pts += task_imp_pts
        self.total_pts += task_imp_pts
        self.urg_pts += task_urg_pts
        self.total_pts += task_urg_pts

    def lose_points(self, task_urg_pts=29, task_imp_pts=29):
        pass
        self.imp_pts -= task_imp_pts
        self.total_pts -= task_imp_pts
        self.urg_pts -= task_urg_pts
        self.total_pts -= task_urg_pts

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
            self.avatar_mode = 'wildanimals_'
        else:
            pass  

    def update_avatar(self):
        pass
        img_key = int(self.urg_perc)

        responsive = 53
        resp_n_act = 51
        act_n_resp = 49
        pro_active = 48

        if responsive < img_key:
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
            self.avatar_img = str('avatar' + img_dict[img_key] + '.png')
            print('assigned avatar...')
            print(self.avatar_img)
                db.session.commit()
        else:
            self.avatar_img = 'avatar10.png'
            print(self.avatar_img)
            db.session.commit()

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"



# ===== ====== ===== ====== =====
class Proday(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)

    cat01 = db.Column(db.String(24))
    act01 = db.Column(db.String(48))
    done01 = db.Column(db.Boolean, default=False)

    cat02 = db.Column(db.String(24))
    act02 = db.Column(db.String(48))
    done02 = db.Column(db.Boolean, default=False)

    cat03 = db.Column(db.String(24))
    act03 = db.Column(db.String(48))
    done03 = db.Column(db.Boolean, default=False)

    cat04 = db.Column(db.String(24))
    act04 = db.Column(db.String(48))
    done04 = db.Column(db.Boolean, default=False)

    icon01 = db.Column(db.String(24))
    icon02 = db.Column(db.String(24))
    icon03 = db.Column(db.String(24))
    icon04 = db.Column(db.String(24))

    count_c01 = db.Column(db.Integer, default=int(1))
    count_c02 = db.Column(db.Integer, default=int(1))
    count_c03 = db.Column(db.Integer, default=int(1))
    count_c04 = db.Column(db.Integer, default=int(1))

    countD_c01 = db.Column(db.Integer, default=int(0))
    countD_c02 = db.Column(db.Integer, default=int(0))
    countD_c03 = db.Column(db.Integer, default=int(0))
    countD_c04 = db.Column(db.Integer, default=int(0))

    count_done = db.Column(db.Integer, default=int(0))
    count_total = db.Column(db.Integer, default=int(4))

    perc_done = db.Column(db.Integer, default=int(0))

    message_total = db.Column(db.String(128))

    def __repr__(self):
        return f"Proday ('{self.title}', '{self.desc}')"

    def init_icons(self):
        ''' init icons per user selection of categories '''
        pass
        _dict = {
            '1': 'drafting-compass',
            '2': 'walking',
            '3': 'spa',
            '4': 'battery-quarter',
        }
        self.icon01 = _dict[self.cat01]
        self.icon02 = _dict[self.cat02]
        self.icon03 = _dict[self.cat03]
        self.icon04 = _dict[self.cat04]

    def init_histogram(self):
        ''' counts user-selected actions by categories'''
        all_cats = [
            str(category) for category in range(1, 5)
        ]
        zeros = [
            int(0) for category in all_cats
        ]
        d = dict(zip(all_cats, zeros))
        user_cats = [
            self.cat01, self.cat02, self.cat03, self.cat04,
        ]

        for cat in user_cats:
            if cat not in d:
                d[cat] = 1
            else:
                d[cat] += 1

        self.count_c01 = d.get('1')
        self.count_c02 = d.get('2')
        self.count_c03 = d.get('3')
        self.count_c04 = d.get('4')

    def init_countDone(self):
        ''' vars req'd for progress bar visualization '''
        pass
        CountDonePerCat = [
            self.countD_c01,
            self.countD_c02,
            self.countD_c03,
            self.countD_c04,
        ]
        ones = []
        for count in CountDonePerCat:
            if count == None:
                count = 0
                db.session.commit()
            elif count == 0:
                ones.append(0)
            else:
                ones.append(int(count))

        self.count_done = sum(ones)
        self.count_total = len(CountDonePerCat)
        self.perc_done = int(round(self.count_done/self.count_total*100))

    def update_progress(self):
        'update action completion percentage'
        self.perc_done = int(round(self.count_done/self.count_total*100))

    def random_quote(self):
        'inserts a random msg above list'
        random_integer = random.randint(0, len(list_of_quotes))-1
        self.message_total = list_of_quotes[random_integer]
        print(self.message_total)
        return self.message_total
# ===================================


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    content = db.Column(db.Text)
    done = db.Column(db.Boolean, default=False)
    is_urgent = db.Column(db.Text, default='n')
    is_important = db.Column(db.Text, default='n')
    matrix_zone = db.Column(db.Text, default='00')
    border_style = db.Column(db.Text, default='info')
    urg_points = db.Column(db.Integer, default=int(36))
    imp_points = db.Column(db.Integer, default=int(36))
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def add_matrix_zone(self):
        pass
        self.matrix_zone = str(self.is_urgent) + str(self.is_important)

    def add_task_border(self):
        pass
        style_dict = {'11': 'danger', '10': 'warning',
                      '01': 'primary', '00': 'info'}
        self.border_style = style_dict[self.matrix_zone]

    def add_urgency_points(self):
        pass
        urgency_point_dict = {
            '11': '96',
            '10': '72',
            '01': '48',
            '00': '36',
        }
        self.urg_points = int(urgency_point_dict[self.matrix_zone])

    def add_importance_points(self):
        pass
        importance_point_dict = {
            '11': '96',
            '10': '48',
            '01': '72',
            '00': '36',
        }
        self.imp_points = int(importance_point_dict[self.matrix_zone])

    def __repr__(self):
        return '<Task %s>' % self.title
# ===================================

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
