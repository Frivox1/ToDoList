from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

tasks = []

class Task:
    def __init__(self, id, content, due_date, completed=False):
        self.id = id
        self.content = content
        self.due_date = due_date
        self.completed = completed

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/')
def index():
    tasks.sort(key=lambda t: t.due_date)
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    content = request.form['content']
    due_date = datetime.strptime(request.form['due_date'], '%Y-%m-%d')
    id = len(tasks) + 1
    tasks.append(Task(id, content, due_date))
    return redirect(url_for('index'))

@app.route('/complete/<id>', methods=['POST'])
def complete(id):
    task = next(t for t in tasks if t.id == int(id))
    task.completed = not task.completed
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['POST'])
def edit(id):
    new_content = request.form['content']
    for task in tasks:
        if task.id == id:
            task.content = new_content
            break
    return redirect(url_for('index'))


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    for task in tasks:
        if task.id == id:
            tasks.remove(task)
            break
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)