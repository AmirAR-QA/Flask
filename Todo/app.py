from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__) 

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@35.197.230.179/todolist"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) 

class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100), nullable=False)
    complete = db.Column(db.Boolean, default=False)

@app.route('/')
@app.route('/home')
def home():
    return 'This is a to-do list application!'

@app.route('/new')
def _new():
    todos1 = todos(Task="New To-do", Complete=True)
    db.session.add(todos1)
    db.session.commit()
    return "You've added a new task to do"

@app.route("/complete/<int:id>")
def complete(id):
    todos1 = todos1.query.get(id)
    todos1.complete = True
    db.session.commit()
    return "You've completed the task " + str(id)

@app.route("/incomplete/<int:id>")
def incomplete(id):
    todos1 = todos1.query.get(id)
    todos1.complete = False
    db.session.commit()
    return "You've incompleted the task " + str(id)

@app.route("/delete/<int:id>")
def delete(id):
    todos1 = todos1.query.get(id)
    db.session.delete(todos1)
    db.session.commit()
    return "You've deleted the task " + str(id)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')