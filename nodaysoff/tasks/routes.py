from flask import (render_template, url_for, flash, redirect, request, abort, Blueprint, g)
from flask_login import current_user, login_required
from nodaysoff import db
from nodaysoff.models import Task
from nodaysoff.tasks.forms import TaskForm

tasks = Blueprint('tasks', __name__)

@tasks.route("/h0me")
def h0me():
    pass

    if Task.query.first() == None:
        pass
        tasks = []
        flash('No task to do, impressive!')
    else:
        pass
        page = request.args.get('page', 1, type=int)
        tasks = Task.query.order_by(Task.date_posted.desc()).paginate(page=page, per_page=5)
    
    
    return render_template('h0me.html', tasks=tasks)


# conv from post ex
@tasks.route("/task/new", methods=['GET', 'POST'])
@login_required
def new_task():
    pass
    form = TaskForm()
    
    if form.validate_on_submit():
        task = Task(
            title=form.title.data, 
            content=form.content.data, 
            manag5r=current_user, 
        )
        
        db.session.add(task)
        
        db.session.commit()
        
        flash('Your task has been created!', 'success')
        
        return redirect(url_for('tasks.new_task'))
    
    return render_template('create_task.html', title='New Task',
                           form=form, legend='New Task')


@tasks.route("/task/<int:task_id>")
def task(task_id):
    task = Task.query.get_or_404(task_id)
    return render_template('task.html', title=task.title, task=task)


@tasks.route("/task/<int:task_id>/update", methods=['GET', 'POST'])
@login_required
def update_task(task_id):
    pass
    task = Task.query.get_or_404(task_id)
    if task.author != current_user:
        abort(403)
    form = TaskForm()
    if form.validate_on_submit():
        task.title = form.title.data
        task.content = form.content.data
        db.session.commit()
        flash('Your task has been updated!', 'success')
        return redirect(url_for('tasks.task', task_id=task.id))
    elif request.method == 'GET':
        form.title.data = task.title
        form.content.data = task.content
    return render_template('create_task.html', title='Update Task',
                           form=form, legend='Update Task')

# displays all tasks and info
@tasks.route('/task', methods=['POST', 'GET'])
def tasks_list():
    pass
    current_user.init_avatarmode()
    current_user.init_avatar()
    current_user.update_avatar()
    tasks = Task.query.all()
    return render_template('create_task.html', tasks=tasks)

# form to create task and info
@tasks.route('/t4sk', methods=['POST', 'GET'])
def taskcreator():
    pass
    TaskCreateForm = TaskForm()
    return render_template('create_t4sk.html', form=TaskCreateForm)


# creates a task as well as attiributes for visual details, border colors, points etc
@tasks.route('/task/create', methods=['POST'])
def add_task():
    pass
    task = Task(
        title=request.form["title"],
        content=request.form["content"],
        is_urgent=request.form.get('is_urgent'),
        is_important=request.form["is_important"],
        manag5r=current_user,
        )
    
    # this will be used to determine all object properties later
    task.add_matrix_zone()
    
    # determine border per matrix zone
    task.add_task_border()
    
    # add urgency points for task completion per matrix zone
    task.add_urgency_points()
    
    # add importancy points for task completion per matrix zone
    task.add_importance_points()
    
    flash('Task created!', task.border_style)
    db.session.add(task)
    db.session.commit()
    return redirect('/task')

# strikes task header on interface, updates DB for task status
@tasks.route('/done/<int:task_id>')
def resolve_task(task_id):
    # current_user.init_avatar()
    current_user.init_points()
    current_user.init_percs()
    db.session.commit()
    task = Task.query.get(task_id)
    
    if not task:
        return redirect(url_for('tasks.tasks_list'))
    if task.done:
        task.done = False
        current_user.lose_points(
            task_urg_pts = task.urg_points,
            task_imp_pts = task.imp_points,
        )
        current_user.update_avatar()
        current_user.update_percs()
        db.session.commit()
    else:
        task.done = True
        current_user.gain_points(
            task_urg_pts = task.urg_points,
            task_imp_pts = task.imp_points,
        )
        current_user.update_avatar()
        current_user.update_percs()
        db.session.commit()
    return redirect(url_for('tasks.tasks_list'))
    # return render_template('create_task.html')


# @tasks.route("/task/<int:task_id>/delete", methods=['POST'])
# @login_required
# def delete_task(task_id):
#     task = Task.query.get_or_404(task_id)
#     if task.author != current_user:
#         abort(403)
#     db.session.delete(task)
#     db.session.commit()
#     flash('Your task has been deleted!', 'success')
#     return redirect(url_for('main.home'))


# delete task --> TODO: archive only

@tasks.route('/delete/<int:task_id>')
def delete_task(task_id):
    pass
    task = Task.query.get(task_id)
    if not task:
        return redirect(url_for('tasks.tasks_list'))
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('tasks.tasks_list'))



#     @app.route('/signup', methods=['GET', 'POST'])
# def signup_page():
#     """User sign-up page."""
#     signup_form = SignupForm(request.form)
#     # POST: Sign user in
#     if request.method == 'POST':
#         if signup_form.validate():
#             # Get Form Fields
#             name = request.form.get('name')
#             email = request.form.get('email')
#             password = request.form.get('password')
#             website = request.form.get('website')
#             existing_user = User.query.filter_by(email=email).first()
#             if existing_user is None:
#                 user = User(name=name,
#                             email=email,
#                             password=generate_password_hash(password, method='sha256'),
#                             website=website)
#                 db.session.add(user)
#                 db.session.commit()
#                 login_user(user)
#                 return redirect(url_for('main_bp.dashboard'))
#             flash('A user already exists with that email address.')
#             return redirect(url_for('auth_bp.signup_page'))
#     # GET: Serve Sign-up page
#     return render_template('/signup.html',
#                            title='Create an Account | Flask-Login Tutorial.',
#                            form=SignupForm(),
#                            template='signup-page',
#                            body="Sign up for a user account.")                                                      


@tasks.route("/demo", methods=['POST', 'GET'])
def task_demo():
    TaskCreateForm = TaskForm()
    return render_template('create_t4sk.html', form=TaskCreateForm)

# creates a task as well as attiributes for visual details, border colors, points etc
@tasks.route('/t4sk/create', methods=['POST'])
def add_t4sk():
    pass
    login_manager.anonymous_user = MyAnonymousUser
    task = Task(
        title=request.form["title"],
        content=request.form["content"],
        is_urgent=request.form.get('is_urgent'),
        is_important=request.form["is_important"],
        manag5r=current_user,
        )
    task.add_matrix_zone()
    task.add_task_border()
    task.add_urgency_points()
    task.add_importance_points()
    flash('Task created!', task.border_style)
    db.session.add(task)
    db.session.commit()
    return redirect('/task/demo')
