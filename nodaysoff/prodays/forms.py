from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired


class ProDayForm(FlaskForm):
    title = StringField('A Productive Day', validators=[DataRequired()])
    
    desc = StringField('Description', validators=[DataRequired()])
    
    cat01 = SelectField('Category', choices = [('1', 'Mind'), ('2', 'Body'), 
                                   ('3', 'Spirit'), ('4', 'Recharge')])    
    act01 = StringField('An Action', validators=[DataRequired()])

    cat02 = SelectField('Category', choices = [('1', 'Mind'), ('2', 'Body'), 
                                ('3', 'Spirit'), ('4', 'Recharge')])    
    act02 = StringField('An Action', validators=[DataRequired()])

    cat03 = SelectField('Category', choices = [('1', 'Mind'), ('2', 'Body'), 
                            ('3', 'Spirit'), ('4', 'Recharge')])    
    act03 = StringField('An Action', validators=[DataRequired()])

    cat04 = SelectField('Category', choices = [('1', 'Mind'), ('2', 'Body'), 
                            ('3', 'Spirit'), ('4', 'Recharge')])        
    act04 = StringField('An Action', validators=[DataRequired()])        
