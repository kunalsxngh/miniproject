
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class TaskForm(FlaskForm):
    name = StringField('Name of task', validators=[
        DataRequired(),
    ])
    submit = SubmitField('Save task')

class updateTask(FlaskForm):
    oldTask = StringField('Old task', validators=[
        DataRequired(),
    
    ])
    newTask = StringField('New task', validators=[
        DataRequired(),
    ])
    submit = SubmitField('Update task')