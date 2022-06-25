# /**
#  *
#  * project name : dp todo application
#  * author name  : mindula dilthushan
#  * author email : minduladilthushan1@gmail.com
#  *
#  */
from flask import Flask, request, session
from flask_sqlalchemy import SQLAlchemy
import os.path

# database path ----------------------------
database_path = os.path.join(os.path.dirname(__file__), 'db/dp_todo.db')

app = Flask(__name__)

# database config --------------------------
app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{database_path}'
database = SQLAlchemy(app)


class Task(database.Model):
    dp_id = database.Column(database.Integer, primary_key=True)
    dp_task = database.Column(database.String(250), nullable=False)
    dp_done = database.Column(database.Boolean(), default=False)

    def __repr__(self):
        return '<User %r>' % self.dp_task


# database create ------------------------------
database.create_all()


@app.route('/create')
def create_task():
    task_name = request.args["task"]
    task = Task(dp_task=task_name)
    database.session.add(task)
    database.session.commit()
    return "Done"


@app.route('/')
def root_route():
    all_tasks = Task.query.all()
    task_list = ""
    for t in all_tasks:
        task_list = f"<p> {t.dp_id} - {t.dp_task} - {'[ ]' if not t.dp_done else '[X]'} </p>"

    return f"<p> Task List </p> {task_list}"


if __name__ == '__main__':
    app.run()
