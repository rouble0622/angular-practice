import jwt
from datetime import datetime, timedelta
from flask import current_app
from functools import wraps
from flask import request, jsonify
from app.models.user import User

def create_access_token(identity):
    """Create a new JWT access token."""
    payload = {
        'user_id': identity,
        'exp': datetime.utcnow() + timedelta(seconds=current_app.config['JWT_ACCESS_TOKEN_EXPIRES']),
        'iat': datetime.utcnow()
    }
    return jwt.encode(
        payload,
        current_app.config['JWT_SECRET_KEY'],
        algorithm='HS256'
    )

def jwt_required(fn):
    """Decorator to protect routes with JWT authentication."""
    @wraps(fn)
    def wrapper(*args, **kwargs):
        token = None
        
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]
            
        if not token:
            return jsonify({'error': 'Token is missing'}), 401
            
        try:
            payload = jwt.decode(
                token,
                current_app.config['JWT_SECRET_KEY'],
                algorithms=['HS256']
            )
            request.user_id = payload['user_id']
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token'}), 401
            
        return fn(*args, **kwargs)
    return wrapper

def role_required(role_name):
    """Decorator to check if user has required role."""
    def decorator(fn):
        @wraps(fn)
        @jwt_required
        def wrapper(*args, **kwargs):
            user = User.query.get(request.user_id)
            if not user:
                return jsonify({'error': 'User not found'}), 404
                
            if not user.has_role(role_name):
                return jsonify({'error': 'Insufficient permissions'}), 403
                
            return fn(*args, **kwargs)
        return wrapper
    return decorator 