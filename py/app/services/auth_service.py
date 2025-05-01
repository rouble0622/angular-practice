from app.models.user import User
from app import db
from typing import Optional, Tuple

class AuthService:
    @staticmethod
    def create_user(username: str, email: str, password: str) -> Tuple[User, str]:
        """Create a new user and return the user object and any error message."""
        if User.query.filter_by(username=username).first():
            return None, "Username already exists"
            
        if User.query.filter_by(email=email).first():
            return None, "Email already exists"
            
        user = User(username=username, email=email)
        user.set_password(password)
        
        try:
            db.session.add(user)
            db.session.commit()
            return user, None
        except Exception as e:
            db.session.rollback()
            return None, str(e)

    @staticmethod
    def authenticate_user(username: str, password: str) -> Optional[User]:
        """Authenticate a user by username and password."""
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            return user
        return None

    @staticmethod
    def get_user_by_id(user_id: int) -> Optional[User]:
        """Get a user by their ID."""
        return User.query.get(user_id)