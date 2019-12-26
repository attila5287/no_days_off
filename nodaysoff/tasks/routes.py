from flask import (render_template, url_for, flash, redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from nodaysoff import db
from nodaysoff.models import Task
from nodaysoff.tasks.forms import TaskForm

tasks = Blueprint('tasks', __name__)
# db.create_all()

@tasks.route("/task/new", methods=['GET', 'POST'])
@login_required
def new_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(task)
        db.session.commit()
        flash('Your task has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_task.html', title='New Task',
                           form=form, legend='New Task')


@tasks.route("/task/<int:task_id>")
def task(task_id):
    task = Task.query.get_or_404(task_id)
    return render_template('task.html', title=task.title, task=task)


@tasks.route("/task/<int:task_id>/update", methods=['GET', 'POST'])
@login_required
def update_task(task_id):
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

# displays single task on update
@tasks.route('/task', methods=['POST', 'GET'])
def tasks_list():
    pass
    TaskCreateForm = TaskForm()
    tasks = Task.query.all()
    return render_template('create_task.html', tasks=tasks, TaskForm=TaskCreateForm)


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
    return redirect('/')


# # delete task --> TODO: archive only

# @tasks.route('/delete/<int:task_id>')
# def delete_task(task_id):
#     pass
#     task = Task.query.get(task_id)
#     if not task:
#         return redirect(url_for('tasks.tasks_list'))
#     db.session.delete(task)
#     db.session.commit()
#     return redirect(url_for('tasks.tasks_list'))

# strikes task header on interface, updates DB for task status
@tasks.route('/done/<int:task_id>')
def resolve_task(task_id):
    task = Task.query.get(task_id)

    if not task:
        return redirect(url_for('tasks.tasks_list'))
    if task.done:
        task.done = False
    else:
        task.done = True

    db.session.commit()
    return redirect(url_for('tasks.tasks_list'))


@tasks.route("/task/<int:task_id>/delete", methods=['POST'])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.author != current_user:
        abort(403)
    db.session.delete(task)
    db.session.commit()
    flash('Your task has been deleted!', 'success')
    return redirect(url_for('main.home'))