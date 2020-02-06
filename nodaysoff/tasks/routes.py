from flask import (render_template, url_for, flash, redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from nodaysoff import db
from nodaysoff.models import Task, UserDemo, TaskDemo
from nodaysoff.tasks.forms import TaskForm, TaskDemoForm

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
    form = ProdayForm()
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


# creates a task as well as attributes for visual details, border olors, points etc
@tasks.route('/task/create', methods=['POST'])
def add_task():
    pass
    print('test')
    print(request.form["title"])
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
    
    flash('Task created! anon user', task.border_style)
    db.session.add(task)
    db.session.commit()
    return redirect('/t4sk')

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


@tasks.route('/delete/<int:task_id>')
def delete_task(task_id):
    pass
    task = Task.query.get(task_id)
    if not task:
        return redirect(url_for('tasks.tasks_list'))
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('tasks.tasks_list'))


@tasks.context_processor
def utility_processor():
    ''' need it to handle demo tasks w/o database inv. due to sql-inj concerns '''
    pass
    tasks = [
        TaskDemo(title=Title, content=Content, is_urgent=IsUrgent, is_important=IsImportant) for (Title, Content, IsUrgent, IsImportant) in zip(
            [
                'urgent and important task',
                'urgent but not-so-important',
                'not-so-urgent but important',
                'neither-so-impt nor-so-urgent',
            ],
            [
                'these tasks have the highest points',
                'the more you complete the tasks',
                'the more points you collect',
                'hence change the avatar -> Task-Hero'
            ],
            [1,1,0,0],
            [1,0,1,0]
        )
    ]
    return dict(TaskDemoList=tasks)

@tasks.context_processor
def inject_style_dict():
    pass
    style_dict = {
        '11': 'danger', '10': 'warning', '01': 'primary', '00': 'info'
    }
    return dict(style_dict=style_dict)

@tasks.context_processor
def inject_urgpts_dict():
    pass
    urgency_point_dict = {
        '11': '96',
        '10': '72',
        '01': '48',
        '00': '36',
    }
    return dict(urgency_point_dict=urgency_point_dict)

@tasks.context_processor
def inject_imppts_dict():
    pass
    importance_point_dict = {
        '11': '96',
        '10': '48',
        '01': '72',
        '00': '36',
    }
    return dict(importance_point_dict=importance_point_dict)

# ========= HOME PAGE FOR DEMO ===========
@tasks.route("/taskdemo/home", methods=['POST', 'GET'])
def task_demo_home():
    pass
    TaskDemoF0rm = TaskDemoForm()
    DemoUser = UserDemo()

    flash('Welcome to Task Hero-demo!', 'warning')
    
    if request.method == 'POST':
        pass
        taskDemo = TaskDemo(
        title=request.form.get('title'),
        content=request.form.get('content'),
        is_urgent=request.form.get('is_urgent'),
        is_important=request.form.get('is_important'),
        )
        tasks.append(taskDemo)
        flash('TaskDemo created!', taskDemo.border_style)
        print(taskDemo)
        return redirect(url_for('tasks.task_demo_home'))

    return render_template(
        'taskdemohome.html',
        form=TaskDemoF0rm,
        DemoUser=DemoUser,
    )


# ====== CREATES A TASK OBJECT REDIRECTS BACK TO ABOVE>>DEMO-HOME ======
@tasks.route('/taskdemo/taskcreator', methods=['POST'])
def task_demo_gen():
    pass
    

@tasks.route('/d0ne/<int:task_id>')
def taskdemodone(task_id):
    task = Task.query.get(task_id)
    urg_points = task.urg_points
    imp_points = task.imp_points
    if task.done:
        task.done = False
        DemoUser.lose_points(
            task_urg_pts=urg_points,
            task_imp_pts = imp_points,
        )
        DemoUser.update_avatar()
        DemoUser.update_percs()
    else:
        task.done = True
        DemoUser.gain_points(
            task_urg_pts = urg_points,
            task_imp_pts = imp_points,
        )
        DemoUser.update_avatar()
        DemoUser.update_percs()
    return redirect(url_for('tasks.task_demo_home'))
