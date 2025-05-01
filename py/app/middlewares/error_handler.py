from flask import jsonify
from werkzeug.exceptions import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from app import db

def register_error_handlers(app):
    @app.errorhandler(HTTPException)
    def handle_http_error(error):
        response = {
            'error': error.description,
            'status_code': error.code
        }
        return jsonify(response), error.code

    @app.errorhandler(SQLAlchemyError)
    def handle_db_error(error):
        db.session.rollback()
        response = {
            'error': 'Database error occurred',
            'status_code': 500
        }
        return jsonify(response), 500

    @app.errorhandler(Exception)
    def handle_generic_error(error):
        response = {
            'error': str(error),
            'status_code': 500
        }
        return jsonify(response), 500 