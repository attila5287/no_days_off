from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired


class ProDayForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()], default='A Productive Day')
    
    desc = StringField('Description', validators=[DataRequired()], default='a new day')
    
    cat01 = SelectField('Category', choices = [('1', 'Mind'), ('2', 'Body'), 
                                   ('3', 'Spirit'), ('4', 'Recharge')], default='1')    
    act01 = StringField('An Action', validators=[DataRequired()], default='test action')

    cat02 = SelectField('Category', choices = [('1', 'Mind'), ('2', 'Body'), 
                                ('3', 'Spirit'), ('4', 'Recharge')], default='2')    
    act02 = StringField('An Action', validators=[DataRequired()], default='test action')

    cat03 = SelectField('Category', choices = [('1', 'Mind'), ('2', 'Body'), 
                            ('3', 'Spirit'), ('4', 'Recharge')], default='3')    
    act03 = StringField('An Action', validators=[DataRequired()], default='test action')

    cat04 = SelectField('Category', choices = [('1', 'Mind'), ('2', 'Body'), 
                            ('3', 'Spirit'), ('4', 'Recharge')], default='4')        
    act04 = StringField('An Action', validators=[DataRequired()], default='test action')        


