from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    pass
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    is_urgent = SelectField(choices=[('0', 'n'), ('1', 'y')])
    is_important = SelectField(choices=[('0', 'n'), ('1', 'y')])
    submit = SubmitField('List Task!')
    
 
class TaskDemoForm(FlaskForm):
    pass
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    is_urgent = SelectField(choices=[('0', 'n'), ('1', 'y')])
    is_important = SelectField(choices=[('0', 'n'), ('1', 'y')])
    submit = SubmitField('List Task!')
    