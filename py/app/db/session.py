from app import db
from contextlib import contextmanager

@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    try:
        yield db.session
    except Exception as e:
        db.session.rollback()
        raise e
    finally:
        db.session.close()

def init_db():
    """Initialize the database."""
    db.create_all() 