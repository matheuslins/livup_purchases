from contextlib import contextmanager

from flask_sqlalchemy import SQLAlchemy
from flask import current_app

from src.settings import DATABASE


db = SQLAlchemy()


class DBHandler:

    def __init__(self, app):
        self.app = app
        self.db_default = f"postgresql://{DATABASE['DB_USER']}:{DATABASE['DB_PASSWORD']}" \
               f"@{DATABASE['DB_HOST']}/{DATABASE['DB_NAME']}"

    def init_db(self):
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['SQLALCHEMY_DATABASE_URI'] = self.db_default
        self.app.config['SQLALCHEMY_BINDS'] = {'default': self.db_default}
        db.init_app(self.app)


@contextmanager
def async_session():
    session = db.create_scoped_session(
        options=dict(bind=db.get_engine(current_app, 'default'), binds={})
    )
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
