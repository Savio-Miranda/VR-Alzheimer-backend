import os

from flask import Flask
from blueprints.patients import init_app as init_patients
from blueprints.users import init_app as init_users
from blueprints.evaluation import init_app as init_evaluation
from database.model import init_app as init_db
from database.serializer import init_app as init_serializer
from database.migrate import init_app as init_migrate

def create_app():
    app = Flask(__name__)
    init_users(app)
    init_patients(app)
    init_evaluation(app)
    init_db(app)
    init_serializer(app)
    init_migrate(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0')
