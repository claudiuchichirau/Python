from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from controllers import create_user, authenticate_user, check_username

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/Proiect_Python'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    salt = db.Column(db.String(100), nullable=False)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), db.ForeignKey('password.username'), nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Adaugă aici modelele pentru baza de date

# Adaugă rutele pentru controlere
app.add_url_rule('/create_user', 'create_user', create_user, methods=['POST'])
app.add_url_rule('/authenticate_user', 'authenticate_user', authenticate_user, methods=['POST'])
app.add_url_rule('/check_username', 'check_username', check_username, methods=['POST'])



if __name__ == '__main__':
    # with app.app_context():
    #     print("s-au creat")
    #     db.create_all()
    app.run(debug=True)
