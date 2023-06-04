from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
    app.config['SECRET_KEY'] = 'my-super-duper-secrect-key'
    UPLOAD_FOLDER       = 'project/static/img'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    db.init_app(app)
    migrate = Migrate(app, db)
    from .main import main
    app.register_blueprint(main)

    return app
