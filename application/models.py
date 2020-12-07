from application import db

"""class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    tasks = db.relationship('Tasks', backref='user')
"""
class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    completed = db.Column(db.Boolean, default = False)
    #user_id = db.Column(db.Integer, db.Foreign('users.id'), nullable=False)