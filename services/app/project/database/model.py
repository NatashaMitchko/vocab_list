from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import ENUM as pgEnum
from enum import Enum, unique

db = SQLAlchemy()


@unique
class UserStatus(Enum):
    pending = "PENDING"
    active = "ACTIVE"
    inactive = "INACTIVE"
    suspended = "SUSPENDED"
    banned = "BANNED"

    def __repr__(self):
        return f"{str.upper(self.name)}"


@unique
class UserTier(Enum):
    admin = "ADMIN"
    regular = "REGULAR"

    def __repr__(self):
        return f"{str.upper(self.name)}"


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
        db.UniqueConstraint(
            "user_id", "book_id", "title", postgresql_nulls_not_distinct=True
        ),
    )

    id = db.Column(db.Integer, autoincrement=True, nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=True)
    title = db.Column(db.String(128), nullable=True)


class ListWordORM(db.Model):
    __tablename__ = "list_words"
    __table_args__ = (db.UniqueConstraint("list_id", "word_id"),)

    id = db.Column(db.Integer, autoincrement=True, nullable=False, primary_key=True)
    list_id = db.Column(db.Integer, db.ForeignKey("lists.id"))
    word_id = db.Column(db.Integer, db.ForeignKey("words.id"))

    list = db.relationship("ListORM", backref="list_words")
    word = db.relationship("WordORM", backref="list_words")
