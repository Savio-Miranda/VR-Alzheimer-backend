from flask import Blueprint

bp_patients = Blueprint('patients', __name__)


def init_app(app):
    app.register_blueprint(bp_patients)


@bp_patients.route('/api/patients', methods=['POST'])
def create():
    return ''


@bp_patients.route('/api/patients', methods=['GET'])
def read():
    return ""


@bp_patients.route('/api/patients', methods=['PUT'])
def update():
    return ""


@bp_patients.route("/api/patients", methods=['DELETE'])
def delete():
    return ""