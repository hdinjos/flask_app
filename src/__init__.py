import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from src.config import config
from dotenv import load_dotenv


db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app(config_name=None):

    if (config_name is None):
        config_name = os.getenv("FLASK_CONFIG", "development")

    app = Flask(__name__)

    app.config.from_object(config[config_name])

    db.init_app(app)
    migrate.init_app(app, db)

    @app.route("/")
    def index():
        return "Hello World"

    from src.views import users
    app.register_blueprint(users.bp)

    return app
