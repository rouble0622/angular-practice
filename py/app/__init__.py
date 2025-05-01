from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config
from .logger import setup_logger
from flask_restx import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager
# import pymysql
# pymysql.install_as_MySQLdb()

db = SQLAlchemy()
migrate = Migrate()
api = Api(
    title='My Flask API',
    version='1.0',
    description='A simple API with JWT Auth and Role-based Access',
    doc='/docs'  # Swagger UI at /docs
)
jwt = JWTManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Initialize CORS with proper configuration
    CORS(app, 
         resources={r"/*": {"origins": ["http://localhost:4200"]}},
         supports_credentials=True,
         allow_headers=["Content-Type", "Authorization"])

    # Initialize API with CORS and error handlers
    api.init_app(app)

    # Setup logging
    setup_logger(app)

    # Register blueprints and namespaces
    from app.routes import auth
    app.register_blueprint(auth.bp)

    from app.routes.protected import api as protected_ns
    api.add_namespace(protected_ns, path='/api')

    # Register CLI commands
    from app.cli import init_roles_command
    app.cli.add_command(init_roles_command)

    return app