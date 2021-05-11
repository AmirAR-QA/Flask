from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__) 

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@35.242.146.124:3306/potato"
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

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')