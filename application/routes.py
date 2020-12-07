from application import app, db
from application.models import Tasks

@app.route('/add/<name>')
def add(name):
    new_task = Tasks(name=name)
    db.session.add(new_task)
    db.session.commit()
    return "Task added."

@app.route('/read')
def read():
    all_tasks = Tasks.query.all()
    tasks_string = ""
    for task in all_tasks:
        tasks_string += "<br>" + task.name +  task.completed
    return tasks_string

@app.route(/update/<name>/<newname>)
def update(name, newname):
    task = Task.query.filter_by(name=name).first()
    task.name = newname
    db.session.commit()
    return task.name

@app.route(/status/<name>/<status>)
def status(name, status):
      task = Task.query.filter_by(name=name).first()
      task.completed = status
      db.session.commit()
      return task.completed

@app.route(/delete/<name>)
def delete(name):
    task_to_delete = Tasks.query.filter_by(name=name).first()
    db.session.delete(task_to_delete)
    db.session.commit()