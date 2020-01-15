from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired


class ProDayForm(FlaskForm):
    title = StringField('A Productive Day', validators=[DataRequired()])
    desc = StringField('Description', validators=[DataRequired()])
    cat01 = SelectField(choices = [('0', 'Mind'), ('1', 'Body'), 
                                   ('2', 'Spirit'), ])
    act01 = StringField('An Action', validators=[DataRequired()])
    cat02 = SelectField(choices = [('0', 'Mind'), ('1', 'Body'), 
                                   ('2', 'Spirit'), ])
    act02 = StringField('Another One', validators=[DataRequired()])
    cat03 = SelectField(choices = [('0', 'Mind'), ('1', 'Body'), 
                                   ('2', 'Spirit'), ])
    act03 = StringField('Again An Action', validators=[DataRequired()])  
    cat04 = SelectField(choices = [('0', 'Mind'), ('1', 'Body'), 
                                   ('2', 'Spirit'), ])
    act04 = StringField('Again An Action', validators=[DataRequired()])  
            
    
    submit = SubmitField('go PR0!')

# class Activity(FlaskForm):
#     pass
