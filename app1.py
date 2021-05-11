from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

app1 = Flask(__name__)

app1.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@35.242.146.124:3306/potato" # Set the connection string to connect to the database
app1.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app1) 

class Countries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    cities = db.relationship('Cities', backref='country') 

class Cities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)

if __name__=='__main__':
    app1.run(debug==True, host='0.0.0.0')