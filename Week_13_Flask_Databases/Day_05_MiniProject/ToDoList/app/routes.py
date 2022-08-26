from flask import render_template, request, url_for, redirect
from app import app, db, models

@app.route('/', methods=("GET", "POST"))
def index():
    if request.method == 'POST':
        task =  models.ToDo(description=request.form['task-description'])
        task.save_task_to_db()
        return redirect(url_for('index'))
    else:
        tasks = models.ToDo.query.all()
        return render_template('index.html', tasks=tasks)


@app.route('/complete/<int:task_id>')
def complete(task_id):
    task = models.ToDo.query.filter_by(id=task_id).first()
    task.complete_task()
    return redirect(url_for('index'))


@app.route('/delete/<int:task_id>')
def delete(task_id):
    models.ToDo.query.filter_by(id=task_id).delete()
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/clear_db')
def clear_db():
    models.ToDo.query.delete()
    db.session.commit()
    return redirect(url_for('index'))