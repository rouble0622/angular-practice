from flask_restx import Resource, Namespace
from app.core.auth import jwt_required, role_required
from flask import jsonify

# Create namespace
api = Namespace('api', description='Protected endpoints')

@api.route('/protected')
class Protected(Resource):
    @api.doc('protected_route')
    @jwt_required
    def get(self):
        """Access protected route"""
        from flask import request
        from app.models.user import User
        
        user = User.query.get(request.user_id)
        return {
            'message': f'Welcome {user.username}!',
            'roles': [role.name for role in user.roles]
        }

@api.route('/admin')
class Admin(Resource):
    @api.doc('admin_route')
    @role_required('admin')
    def get(self):
        """Access admin route"""
        from flask import request
        from app.models.user import User
        
        user = User.query.get(request.user_id)
        return {
            'message': f'Hello {user.username}, you are an admin.'
        }

@api.route('/user-dashboard')
class UserDashboard(Resource):
    @api.doc('user_dashboard')
    @role_required('user')
    def get(self):
        """Access user dashboard"""
        from flask import request
        from app.models.user import User
        
        user = User.query.get(request.user_id)
        return {
            'message': f'Hello {user.username}, welcome to your dashboard.'
        } 