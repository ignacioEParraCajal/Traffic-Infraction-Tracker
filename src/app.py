from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from src.conf import config
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    from src.routes import main_bp
    app.register_blueprint(main_bp)

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
