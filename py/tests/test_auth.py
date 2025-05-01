import pytest
from app import create_app, db
from app.models.user import User
from app.config import Config

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

@pytest.fixture
def app():
    app = create_app(TestConfig)
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_register(client):
    response = client.post('/register', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'Test123!@#'
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['username'] == 'testuser'
    assert 'password' not in data

def test_login(client):
    # First register a user
    client.post('/register', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'Test123!@#'
    })
    
    # Then try to login
    response = client.post('/login', json={
        'username': 'testuser',
        'password': 'Test123!@#'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert 'access_token' in data
    assert data['user']['username'] == 'testuser' 