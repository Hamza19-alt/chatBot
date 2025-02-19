from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_input = db.Column(db.String(500))
    bot_response = db.Column(db.String(500))
#gestion de base de données