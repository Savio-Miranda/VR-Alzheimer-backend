from flask import Blueprint, request, current_app
from database.model import Patients, Users
from database.serializer import PatientsSchema, EvaluationSchema
import json

bp_patients = Blueprint('patients', __name__)


def init_app(app):
    app.register_blueprint(bp_patients)


@bp_patients.route('/api/patients', methods=['POST'])
def create():
    patient_json = request.json
    print("patiente_json: ", patient_json)
    ps = PatientsSchema()
    user = Users.query.get(patient_json['user_id'])
    del patient_json['user_id']
    patient_db = ps.load(patient_json)
    print("patiente_db: ", patient_db)
    user.patients.append(patient_db)
    current_app.db.session.add(patient_db)
    current_app.db.session.commit()
    return ps.jsonify(patient_db)


@bp_patients.route('/api/patients', methods=['GET'])
def read_all():
    ps = PatientsSchema(many=True)
    patients = Patients.query.all()
    return ps.jsonify(patients)


@bp_patients.route('/api/patients/<id>', methods=['GET'])
def read_one(id):
    ps = PatientsSchema()
    patient = Patients.query.get(id)
    if patient is None:
        return {'message': 'patient not found'}, 404
    return ps.jsonify(patient)

@bp_patients.route('/api/patients/<id>/evaluation', methods=['GET'])
def read_evaluation(id):
    es = EvaluationSchema()
    patient = Patients.query.get(id)
    if patient is None:
        return {'message': 'patient not found'}, 404
    evaluation = [json.loads(es.dumps(e)) for e in patient.evaluation]
    return es.jsonify(evaluation)

@bp_patients.route('/api/patients', methods=['PUT'])
def update():
    patient_json = request.json
    ps = PatientsSchema()
    patient_db = Patients.query.filter(Patients.id == patient_json['id'])
    patient_db.update(patient_json)
    current_app.db.session.commit()
    return patient_json


@bp_patients.route("/api/patients", methods=['DELETE'])
def delete():
    patient_json = request.json
    ps = PatientsSchema()
    patient_db = Patients.query.filter(Patients.id == patient_json['id'])
    # patients = patient_db.patients
    # for p in patients:
    #     evaluations = p.evaluations
    #     for e in evaluations:
    #         e.delete()
    #     p.delete()
    patient_db.delete()
    current_app.db.session.commit()
    return {'message': 'patient deleted successfully'}