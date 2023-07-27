from sqlalchemy import create_engine
from models import Dog

SQLITE_URL = "sqlite:///:memory:"
engine = create_engine(SQLITE_URL)


def create_table(base, engine):
    sql = """CREATE TABLE IF NOT EXISTS dogs(
        id INTEGER PRIMARY KEY,
        name TEXT,
        breed TEXT
        );
        """
    return engine


create_table(Dog, engine)


def save(session, dog):
    session.add(dog)
    session.commit()
    return session


def get_all(session):
    pass


def find_by_name(session, name):
    pass


def find_by_id(session, id):
    pass


def find_by_name_and_breed(session, name, breed):
    pass


def update_breed(session, dog, breed):
    pass
