from flask import Blueprint

bp_users = Blueprint('users', __name__)


def init_app(app):
    app.register_blueprint(bp_users)


@bp_users.route('/api/users', methods=['POST'])
def create():
    return ''


@bp_users.route('/api/users', methods=['GET'])
def read():
    return "deu certo"


@bp_users.route('/api/users', methods=['PUT'])
def update():
    return ""


@bp_users.route("/api/users", methods=['DELETE'])
def delete():
    return ""