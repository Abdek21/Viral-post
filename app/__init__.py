from flask import Flask
from flask_cors import CORS
from .config import Config
from .routes import main
from .celery_config import make_celery
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    app.register_blueprint(main)
    
    celery = make_celery(app)
    return app, celery
