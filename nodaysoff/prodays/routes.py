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
        Proday.date_posted.desc()).paginate(page=page, per_page=1)
    if prodays == None:
        prodays = []
    else:
        pass

    return render_template('hom3.html', prodays=prodays)


@prodays.route("/proday/create", methods=['POST'])
@login_required
def create_proday():
    proday = Proday(title=request.form["title"], desc=request.form["desc"], cat01=request.form["cat01"], act01=request.form["act01"], cat02=request.form["cat02"],
                    act02=request.form["act02"], cat03=request.form["cat03"], act03=request.form["act03"], cat04=request.form["cat04"], act04=request.form["act04"], planner=current_user)
    db.session.add(proday)
    db.session.commit()
    flash('Your proday has been created!', 'success')
    return redirect(url_for('prodays.hom3'))


@prodays.route("/proday/new", methods=['GET', 'POST'])
@login_required
def new_proday():
    form = ProDayForm()

    return render_template('create_proday.html', title='New ProDay', form=form)


@prodays.route("/proday/<int:proday_id>")
def proday(proday_id):
    proday = Proday.query.get_or_404(proday_id)
    return render_template('proday.html', title=proday.title, proday=proday)


@prodays.route("/proday/<int:proday_id>/update", methods=['GET', 'POST'])
@login_required
def update_proday(proday_id):
    proday = Proday.query.get_or_404(proday_id)
    if proday.planner != current_user:
        abort(403)
    form = ProDayForm()
    if form.validate_on_submit():
        proday.title=request.form["title"]
        proday.desc=request.form["desc"]
        proday.cat01=request.form["cat01"]
        proday.act01=request.form["act01"]
        proday.cat02=request.form["cat02"]
        proday.act02=request.form["act02"]
        proday.cat03=request.form["cat03"]
        proday.act03=request.form["act03"]
        proday.cat04=request.form["cat04"]
        proday.act04=request.form["act04"]
        db.session.commit()
        flash('Your proday has been updated!', 'success')
        return redirect(url_for('prodays.proday', proday_id=proday.id))
    elif request.method == 'GET':
        pass
        form.title.data = proday.title
        form.desc.data = proday.desc
        form.cat01.data = proday.cat01
        form.act01.data = proday.act01
        form.cat02.data = proday.cat02
        form.act02.data = proday.act02
        form.cat03.data = proday.cat03
        form.act03.data = proday.act03
        form.cat04.data = proday.cat04
        form.act04.data = proday.act04
        
    return render_template('create_proday.html', title='Update Proday',
                           form=form, legend='Update ProDay')


@prodays.route("/proday/<int:proday_id>/delete", methods=['POST'])
@login_required
def delete_proday(proday_id):
    proday = Proday.query.get_or_404(proday_id)
    if proday.planner != current_user:
        abort(403)
    db.session.delete(proday)
    db.session.commit()
    flash('Your proday has been deleted!', 'success')
    return redirect(url_for('main.home'))
