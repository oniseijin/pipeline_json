from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy


# Database setup
db = SQLAlchemy()


def init_app():
    """ Create Flask Application."""

    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('src.config.Config')  # configure app using the Config class defined in src/config.py

    db.init_app(app)  # initialise the database for the app

    with app.app_context():
        from src.models.models import Pipeline  # this import allows us to create the table if it does not exist
        db.create_all()

        from src.pipelines.routes import bp as pipeline_bp
        app.register_blueprint(pipeline_bp)

        return app
