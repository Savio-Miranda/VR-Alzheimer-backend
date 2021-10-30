from flask_migrate import Migrate

mi = Migrate()

def init_app(app):
    mi.init_app(app, app.db)
