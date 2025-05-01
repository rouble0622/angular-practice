from flask import Blueprint, request, jsonify
from app.models.user import User
from app.models.role import Role
from app import db
#from app.core.auth import create_access_token
from app.schemas.user_schema import UserSchema
from flask_jwt_extended import create_access_token

bp = Blueprint('auth', __name__)
user_schema = UserSchema()

@bp.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'error': 'Username already exists'}), 400
        
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already exists'}), 400
    
    #if not data['role'] :
    data['role'] = 'user'

    # Assign default user role
    default_role = Role.query.filter_by(name=data['role'].lower()).first()
    if not default_role:
        return jsonify({'error': 'Role not found'}), 400
    
    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])    
    
    user.roles.append(default_role)
    db.session.add(user)
    db.session.commit()
    
    return jsonify(user_schema.dump(user)), 201

@bp.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Missing username or password'}), 400
        
    user = User.query.filter_by(username=data['username']).first()
    
    if user and user.check_password(data['password']):        
        access_token = create_access_token(identity=user.id)
        return jsonify({
            'access_token': access_token,
            'user': user_schema.dump(user)
        })
    
    return jsonify({'error': 'Invalid username or password'}), 401 