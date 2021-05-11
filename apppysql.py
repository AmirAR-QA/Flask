from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@{insert IP address}/users"

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True)