from flask import Flask
from flask_cors import CORS
from .routes import main_bp
from .config import Database

def create_app():
    app = Flask(__name__)
    CORS(app)
    # Database configuration
    app.config['DB_HOST'] = 'localhost'
    app.config['DB_USER'] = 'root'
    app.config['DB_PASSWORD'] = '@Samclem91'
    
    app.config['DB_NAME'] = 'smartscoop'

    # Initialize database connection
    app.db = Database(
        host=app.config['DB_HOST'],
        user=app.config['DB_USER'],
        password=app.config['DB_PASSWORD'],
        database=app.config['DB_NAME']
    )

    # Register blueprints
    app.register_blueprint(main_bp)

    return app
