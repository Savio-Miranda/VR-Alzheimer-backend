from flask_marshmallow import Marshmallow

from database.model import Users, Patients, Evaluation

ma = Marshmallow()


def init_app(app):
    ma.init_app(app)


class UsersSchema(ma.ModelSchema):
    class Meta:
        model = Users


class PatientsSchema(ma.ModelSchema):
    class Meta:
        model = Patients


class EvaluationSchema(ma.ModelSchema):
    class Meta:
        model = Evaluation
