from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__) # Declare Flask object

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@35.242.146.124:3306/potato2"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) 

class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    purchase = db.relationship('purchase', backref='customers')

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    purchase = db.relationship('purchase', backref='products')

class Purchases(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    purchase_date = db.Column('date', db.String(30))

if __name__=='__main__':
    app.run(debug==True, host='0.0.0.0')