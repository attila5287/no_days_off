from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired



class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    is_urgent = SelectField(choices=[('0', 'n'), ('1', 'y')])
    is_important = SelectField(choices=[('0', 'n'), ('1', 'y')])
    submit = SubmitField('List Task!')
    
    def convert_txt_to_boolean(self):
        pass
        dict = {
            True : bool(1),
            False : bool(0)
        }
        # self.is_urgent = dict[self.is_urgent.data]
        # self.is_important = dict[self.is_important.data]
        print(self.is_urgent.data)
        print(self.is_important.data)
 