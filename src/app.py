from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv


load_dotenv()

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    application = Flask(__name__)
    application.config.from_object('src.conf.Config')

    db.init_app(application)
    migrate.init_app(application, db)

    from src.routes import main
    application.register_blueprint(main)

    return application


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
