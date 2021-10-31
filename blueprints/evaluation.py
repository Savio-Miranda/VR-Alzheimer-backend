from flask import Blueprint, current_app, request
from database.model import Evaluation, Patients
from database.serializer import EvaluationSchema
import json

bp_evaluation = Blueprint('evaluation', __name__)


def init_app(app):
    app.register_blueprint(bp_evaluation)


@bp_evaluation.route('/api/evaluation', methods=['POST'])
def create():
    evaluation_json = request.json
    es = EvaluationSchema()
    patient = Patients.query.get(evaluation_json['patient_id'])
    del evaluation_json['patient_id']
    evaluation_db = es.load(evaluation_json)
    patient.evaluation.append(evaluation_db)
    current_app.db.session.add(evaluation_db)
    current_app.db.session.commit()
    return es.jsonify(evaluation_db)


@bp_evaluation.route('/api/evaluation', methods=['GET'])
def read_all():
    es = EvaluationSchema(many=True)
    evaluation = Evaluation.query.all()
    return es.jsonify(evaluation)


@bp_evaluation.route('/api/evaluation/<id>', methods=['GET'])
def read_one(id):
    es = EvaluationSchema()
    evaluation = Evaluation.query.get(id)
    if evaluation is None:
        return {'message': 'evaluation not found'}, 404
    return es.jsonify(evaluation)

@bp_evaluation.route('/api/evaluation', methods=['PUT'])
def update():
    evaluation_json = request.json
    es = EvaluationSchema()
    evaluation_db = Evaluation.query.filter(Evaluation.id == evaluation_json['id'])
    evaluation_db.update(evaluation_json)
    current_app.db.session.commit()
    return evaluation_json


@bp_evaluation.route("/api/evaluation", methods=['DELETE'])
def delete():
    evaluation_json = request.json
    es = EvaluationSchema()
    evaluation_db = Evaluation.query.filter(Evaluation.id == evaluation_json['id'])
    # evaluation = evaluation_db.evaluation
    # for p in evaluation:
    #     evaluations = p.evaluations
    #     for e in evaluations:
    #         e.delete()
    #     p.delete()
    evaluation_db.delete()
    current_app.db.session.commit()
    return {'message': 'evaluation deleted successfully'}