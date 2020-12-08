from application import app, db
from application.forms import TaskForm, updateTask
from application.models import Tasks
from flask import Flask, render_template, request, redirect, url_for


@app.route('/add', methods = ['GET','POST'])
def add():
    form = TaskForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_task = Tasks(name = form.name.data)
            db.session.add(new_task)
            db.session.commit()
            return  redirect(url_for("home"))
    return render_template('add.html', title="Create a task", form = form)

@app.route('/home', methods = ['GET', 'POST'])
def home():
    all_tasks = Tasks.query.all()
    tasks_string = ""
    return render_template('index.html', title = "Home",all_tasks = all_tasks)


@app.route("/update/<int:id>", methods = ["GET", "POST"])
def update(id):
    form = TaskForm()
    task = Tasks.query.filter_by(id=id).first()
    if request.method == "POST":
        task.name = form.name.data
        db.session.commit()
        return redirect(url_for("home"))

    return render_template('update.html', form = form, name = "Update task", task=task)


@app.route("/delete/<int:id>", methods =['GET', 'POST'])
def delete(id):
    task_to_delete = Tasks.query.filter_by(id=id).first()
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect(url_for("home"))
 