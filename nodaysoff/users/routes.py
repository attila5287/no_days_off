from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from nodaysoff import db, bcrypt
from nodaysoff.models import User, Post
from nodaysoff.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
                                   RequestResetForm, ResetPasswordForm)
from nodaysoff.users.utils import save_picture, send_reset_email

users = Blueprint('users', __name__)



@users.route("/regist3r", methods=['POST'])
def regist3r():
    hashed_password = bcrypt.generate_password_hash(request.form['password'])
    print(hashed_password)
    user = User(
        username=request.form['username'], 
        email=request.form['email'], 
        password=hashed_password,
        urg_pts= 19, 
        imp_pts = 19, 
        total_pts = 38, 
        imp_perc = 50, 
        urg_perc = 50, 
        avatar_mode = 'wildanimals', 
        avatar_img =  'default00.png', 
    )
    db.session.add(user)
    db.session.commit()
    flash('Your account has been created! You are now able to log in', 'success')
    return redirect(url_for('users.login'))


# LET THIS BE THE FORM PAGE ONLY WITH AN EXTRA ROUTE FOR PROCESSING USER-DETAILS
@users.route("/register", methods=['GET', 'POST'])
def register():
    pass
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@users.route("/login", methods=['GET', 'POST'])
def login():
    pass
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        pass
    
        user = User.query.filter_by(email=form.email.data).first()
         
        print('test user obj attributes')
        print(user.password)
        print('test req form pw')
        print(request.form["password"])
        if user and bcrypt.check_password_hash(user.password, request.form["password"]):
            
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.avatar_mode = form.avatar_mode.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.avatar_mode.data = current_user.avatar_mode 
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)


@users.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('user_posts.html', posts=posts, user=user)

@users.route("/user/<string:username>")
def user_prodays(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    prodays = Proday.query.filter_by(planner=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('user_prodays.html', prodays=prodays, user=user)

@users.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', title='Reset Password', form=form)

# =======DELETE TEST USERS
@users.route("/user/<int:user_id>/delete", methods=['GET','POST'])
@login_required
def delete_test_users(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('Test user account has been deleted!', 'success')
    return redirect(url_for('main.home'))