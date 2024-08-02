from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import ENUM as pgEnum
from enum import Enum, unique

db = SQLAlchemy()

@unique
class UserStatus(Enum):
    # pending, active, suspended, banned, inactive
    pending = "PENDING"
    active = "ACTIVE"
    inactive = "INACTIVE"
    suspended = "SUSPENDED"
    banned = "BANNED"

class UserTier(Enum):
    admin = "ADMIN"
    regular = "REGULAR"

class UserORM(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, autoincrement=True, nullable=False, primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    status = db.Column(pgEnum(UserStatus), nullable=False)
    tier = db.Column(pgEnum(UserTier), nullable=False)

class BookORM(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, autoincrement=True, nullable=False, primary_key=True)
    title = db.Column(db.String(128), unique=False, nullable=False)
    author = db.Column(db.String(128), unique=False, nullable=False)
    isbn = db.Column(db.String(128), unique=True, nullable=False)


class WordORM(db.Model):
    __tablename__ = "words"

    id = db.Column(db.Integer, autoincrement=True, nullable=False, primary_key=True)
    word = db.Column(db.String(128), nullable=False)
    part_of_speech = db.Column(db.String(128), nullable=False)
    definition_primary = db.Column(db.String(128), nullable=False)
    definition_secondary = db.Column(db.String(128), nullable=True)


class ListORM(db.Model):
    __tablename__ = "lists"
    __table_args__ = (
        db.UniqueConstraint("user_id", "book_id", "title", postgresql_nulls_not_distinct=True),
      )

    id = db.Column(db.Integer, autoincrement=True, nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=True)
    title = db.Column(db.String(128), nullable=True)


class ListWordORM(db.Model):
    __tablename__ = "list_words"
    __table_args__ = (
        db.UniqueConstraint("list_id", "word_id"),
      )

    id = db.Column(db.Integer, autoincrement=True, nullable=False, primary_key=True)
    list_id = db.Column(db.Integer, db.ForeignKey("lists.id"))
    word_id = db.Column(db.Integer, db.ForeignKey("words.id"))

    list = db.relationship("ListORM", backref="list_words")
    word = db.relationship("WordORM", backref="list_words")

def _create_all():
    db.drop_all()
    db.create_all()
    db.session.commit()

def _seed_all():
    user_1 = UserORM(username="Natasha", status=UserStatus.active, tier=UserTier.admin, password="test", email="a@b.com")
    user_2 = UserORM(username="Nick", status=UserStatus.active, tier=UserTier.regular, password="test", email="c@d.org")
    user_3 = UserORM(username="Alex", status=UserStatus.active, tier=UserTier.regular, password="test", email="e@f.gov")

    book_1 = BookORM(title="Goodnight, Moon", author="me", isbn="1234")

    word_1 = WordORM(word="dog", part_of_speech="noun", definition_primary="", definition_secondary="")
    word_2 = WordORM(word="cat", part_of_speech="noun", definition_primary="", definition_secondary="")
    word_3 = WordORM(word="chicken", part_of_speech="noun", definition_primary="", definition_secondary="")
    word_4 = WordORM(word="cow", part_of_speech="noun", definition_primary="", definition_secondary="")
    word_5 = WordORM(word="pig", part_of_speech="noun", definition_primary="", definition_secondary="")
    word_6 = WordORM(word="camel", part_of_speech="noun", definition_primary="", definition_secondary="")


    list_1 = ListORM(user_id=1, book_id=1, title="first vocab list")
    list_2 = ListORM(user_id=1, book_id=1)

    list_3 = ListORM(user_id=2, title="random words")
    
    list_4 = ListORM(user_id=3)

    listword_1 = ListWordORM(list_id=1, word_id=1)
    listword_2 = ListWordORM(list_id=1, word_id=2)
    listword_3 = ListWordORM(list_id=1, word_id=3)
    listword_4 = ListWordORM(list_id=2, word_id=3)

    listword_5 = ListWordORM(list_id=3, word_id=4)
    listword_6 = ListWordORM(list_id=3, word_id=5)

    listword_7 = ListWordORM(list_id=4, word_id=6)

    db.session.add_all([
        user_1, user_2, user_3,
    ])
    db.session.commit()

    db.session.add_all([
        book_1,
    ])
    db.session.commit()
    
    db.session.add_all([
        word_1, word_2, word_3, word_4, word_5, word_6,
    ])
    db.session.commit()
    
    db.session.add_all([
        list_1, list_2, list_3, list_4,
    ])
    db.session.commit()
    
    db.session.add_all([
        listword_1, listword_2, listword_3, listword_4, listword_5, listword_6, listword_7
    ])
    db.session.commit()

