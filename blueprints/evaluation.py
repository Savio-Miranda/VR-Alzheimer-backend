from flask import Blueprint

bp_evaluation = Blueprint('evaluation', __name__)


def init_app(app):
    app.register_blueprint(bp_evaluation)


@bp_evaluation.route('/api/evaluation', methods=['POST'])
def create():
    return ''


@bp_evaluation.route('/api/evaluation', methods=['GET'])
def read():
    return ""


@bp_evaluation.route('/api/evaluation', methods=['PUT'])
def update():
    return ""


@bp_evaluation.route("/api/evaluation", methods=['DELETE'])
def delete():
    return ""