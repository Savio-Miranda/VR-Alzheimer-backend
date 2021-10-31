from flask import Blueprint, request, current_app, jsonify
from database.serializer import UsersSchema, PatientsSchema
from database.model import Users
import json

bp_users = Blueprint('users', __name__)


def init_app(app):
    app.register_blueprint(bp_users)


@bp_users.route('/api/users', methods=['POST'])
def create():
    user_json = request.json
    us = UsersSchema()
    user_db = us.load(user_json)
    current_app.db.session.add(user_db)
    current_app.db.session.commit()
    return us.jsonify(user_db)


@bp_users.route('/api/users', methods=['GET'])
def read_all():
    us = UsersSchema(many=True)
    users = Users.query.all()
    return us.jsonify(users)


@bp_users.route('/api/users/<id>', methods=['GET'])
def read_one(id):
    us = UsersSchema()
    user = Users.query.get(id)
    if user is None:
        return {'message': 'user not found'}, 404
    return us.jsonify(user)


@bp_users.route('/api/users/<id>/patients', methods=['GET'])
def read_patients(id):
    ps = PatientsSchema()
    user = Users.query.filter(Users.id == id).first()
    print(user)
    if user is None:
        return {'message': 'user not found'}, 404
    patients = [json.loads(ps.dumps(p)) for p in user.patients]
    print("patients: ", patients)
    return jsonify(patients)


@bp_users.route('/api/users', methods=['PUT'])
def update():
    user_json = request.json
    us = UsersSchema()
    user_db = Users.query.filter(Users.id == user_json['id'])
    user_db.update(user_json)
    current_app.db.session.commit()
    return user_json


@bp_users.route("/api/users", methods=['DELETE'])
def delete():
    user_json = request.json
    us = UsersSchema()
    user_db = Users.query.filter(Users.id == user_json['id'])
    # patients = user_db.patients
    # for p in patients:
    #     evaluations = p.evaluations
    #     for e in evaluations:
    #         e.delete()
    #     p.delete()
    user_db.delete()
    current_app.db.session.commit()
    return {'message': 'user deleted successfully'}
