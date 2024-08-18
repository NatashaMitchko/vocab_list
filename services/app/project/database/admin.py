from project.database.model import db, UserORM, BookORM, ListORM, ListWordORM, WordORM
from project.database.user import User
from project.database.list import Word


def get_all_users():
    """
    TODO: pagination support
    (connect this to api routes for datatables)
    """
    db_users = db.session.query(UserORM).all()
    result = []
    for u in db_users:
        result.append(User(u.id, u.username, u.email, u.status, u.tier))
    return result


def get_all_books():
    db_books = db.session.query(BookORM).all()
    return db_books


def get_all_words():
    db_words = db.session.query(WordORM).limit(10)
    result = []
    for w in db_words:
        result.append(
            Word(
                w.id,
                w.word,
                w.part_of_speech,
                w.definition_primary,
                w.definition_secondary,
            )
        )
    return result


"""
List -> get User
List -> get Words
List -> get Book if not null
"""
