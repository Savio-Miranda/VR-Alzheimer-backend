from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
    db.init_app(app)
    app.db = db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(150), nullable=False)
    patients = db.relationship('Patients', backref='users', lazy='select')


class Patients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(150), nullable=False)
    birthdate = db.Column(db.String(150), nullable=False)
    da_stage = db.Column(db.String(150), nullable=False)
    march = db.Column(db.String(150), nullable=False)
    qp_and_hda = db.Column(db.String(150), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    evaluation = db.relationship('Evaluation', backref='patients', lazy='select')


class Evaluation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    evolution = db.Column(db.String(150), nullable=False)
    heigth = db.Column(db.Float, nullable=False)
    width = db.Column(db.Float, nullable=False)
    length = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    evaluation_date = db.Column(db.String(150), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))
