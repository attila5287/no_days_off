from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from nodaysoff import db
from nodaysoff.models import Proday
from nodaysoff.prodays.forms import ProDayForm

prodays = Blueprint('prodays', __name__)


@prodays.route("/hom3")
def hom3():
    page = request.args.get('page', 1, type=int)
    prodays = Proday.query.order_by(
        Proday.date_posted.desc()).paginate(page=page, per_page=5)
    if prodays == None:
        prodays = []
    else:
        pass

    return render_template('hom3.html', prodays=prodays)


@prodays.route("/proday/new", methods=['GET', 'POST'])
@login_required
def new_proday():
    form = ProDayForm()
    if form.validate_on_submit():
        proday = Proday(
            title=request.form["title"],
            content=request.form["content"],
            planner=current_user
            )
        db.session.add(proday)
        db.session.commit()
        flash('Your proday has been created!', 'success')
        return redirect(url_for('prodays.hom3'))
    return render_template('create_proday.html', title='New ProDay',
                           form=form, legend='New ProDay')


@prodays.route("/proday/<int:proday_id>")
def proday(proday_id):
    proday = Proday.query.get_or_404(proday_id)
    return render_template('proday.html', title=proday.title, proday=proday)


@prodays.route("/proday/<int:proday_id>/update", methods=['GET', 'POST'])
@login_required
def update_proday(proday_id):
    proday = Proday.query.get_or_404(proday_id)
    if proday.author != current_user:
        abort(403)
    form = ProDayForm()
    if form.validate_on_submit():
        proday.title = form.title.data
        proday.content = form.content.data
        db.session.commit()
        flash('Your proday has been updated!', 'success')
        return redirect(url_for('prodays.proday', proday_id=proday.id))
    elif request.method == 'GET':
        form.title.data = proday.title
        form.content.data = proday.content
    return render_template('create_proday.html', title='Update Proday',
                           form=form, legend='Update ProDay')


@prodays.route("/proday/<int:proday_id>/delete", methods=['POST'])
@login_required
def delete_proday(proday_id):
    proday = ProDay.query.get_or_404(proday_id)
    if proday.author != current_user:
        abort(403)
    db.session.delete(proday)
    db.session.commit()
    flash('Your proday has been deleted!', 'success')
    return redirect(url_for('main.home'))
