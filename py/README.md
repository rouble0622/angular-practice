# Flask Authentication API

A secure and scalable Flask-based authentication API with JWT token support.

## Features

- User registration and authentication
- JWT token-based authentication
- Password hashing and validation
- SQLAlchemy database integration
- Error handling middleware
- Schema validation with Marshmallow
- Unit tests with pytest

## Project Structure

```
myapp/
│
├── app/                        # Main application package
│   ├── __init__.py            # App factory
│   ├── config.py              # Configuration settings
│   ├── models/                # Database models
│   ├── routes/                # API routes
│   ├── services/              # Business logic
│   ├── db/                    # Database setup
│   ├── core/                  # Core utilities
│   ├── middlewares/           # Middleware
│   ├── schemas/               # Data schemas
│   └── utils/                 # Helper utilities
│
├── tests/                     # Test files
├── migrations/                # Database migrations
├── .env                       # Environment variables
└── requirements.txt           # Project dependencies
```

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with the following variables:
```
SECRET_KEY=your-secret-key
JWT_SECRET_KEY=your-jwt-secret
DATABASE_URL=sqlite:///app.db
```

4. Initialize the database:
```bash
flask db init
flask db migrate
flask db upgrade
```

## Running the Application

```bash
python run.py
```

## API Endpoints

### Authentication

- `POST /register` - Register a new user
- `POST /login` - Login and get JWT token

## Testing

Run tests with pytest:
```bash
pytest
```

## License

MIT 