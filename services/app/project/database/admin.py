from project.database.model import db, UserORM, BookORM, ListORM, ListWordORM, WordORM
from project.database.user import User
from project.database.list import VocabList, Word

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
    result = []
    # for b in db_books:
    #     Book()
    #     result.append()
    return result


def get_all_words():
    list_id = 1
    return []
"""
List -> get User
List -> get Words
List -> get Book if not null
"""