from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, autoincrement=True, nullable=False, primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    email_validated = db.Column(db.Boolean, nullable=False, default=False)


class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, autoincrement=True, nullable=False, primary_key=True)
    title = db.Column(db.String(128), unique=False, nullable=False)
    author = db.Column(db.String(128), unique=False, nullable=False)
    isbn = db.Column(db.String(128), unique=True, nullable=False)


class Word(db.Model):
    __tablename__ = "words"

    id = db.Column(db.Integer, autoincrement=True, nullable=False, primary_key=True)
    word = db.Column(db.String(128), nullable=False)
    part_of_speech = db.Column(db.String(128), nullable=False)
    definition_primary = db.Column(db.String(128), nullable=False)
    definition_secondary = db.Column(db.String(128), nullable=True)


class List(db.Model):
    __tablename__ = "lists"
    __table_args__ = (
        db.UniqueConstraint("user_id", "book_id", "title", postgresql_nulls_not_distinct=True),
      )

    id = db.Column(db.Integer, autoincrement=True, nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=True)
    title = db.Column(db.String(128), nullable=True)


class ListWord(db.Model):
    __tablename__ = "list_words"
    __table_args__ = (
        db.UniqueConstraint("list_id", "word_id"),
      )

    id = db.Column(db.Integer, autoincrement=True, nullable=False, primary_key=True)
    list_id = db.Column(db.Integer, db.ForeignKey("lists.id"))
    word_id = db.Column(db.Integer, db.ForeignKey("words.id"))

    list = db.relationship("List", backref="list_words")
    word = db.relationship("Word", backref="list_words")

def _create_all():
    db.drop_all()
    db.create_all()
    db.session.commit()

def _seed_all():
    user_1 = User(username="Natasha", password="test", email="a@b.com")
    user_2 = User(username="Nick", password="test", email="c@d.org")
    user_3 = User(username="Alex", password="test", email="e@f.gov")

    book_1 = Book(title="Goodnight, Moon", author="me", isbn="1234")

    word_1 = Word(word="dog", part_of_speech="noun", definition_primary="", definition_secondary="")
    word_2 = Word(word="cat", part_of_speech="noun", definition_primary="", definition_secondary="")
    word_3 = Word(word="chicken", part_of_speech="noun", definition_primary="", definition_secondary="")
    word_4 = Word(word="cow", part_of_speech="noun", definition_primary="", definition_secondary="")
    word_5 = Word(word="pig", part_of_speech="noun", definition_primary="", definition_secondary="")
    word_6 = Word(word="camel", part_of_speech="noun", definition_primary="", definition_secondary="")


    list_1 = List(user_id=1, book_id=1, title="first vocab list")
    list_2 = List(user_id=1, book_id=1)

    list_3 = List(user_id=2, title="random words")
    
    list_4 = List(user_id=3)

    listword_1 = ListWord(list_id=1, word_id=1)
    listword_2 = ListWord(list_id=1, word_id=2)
    listword_3 = ListWord(list_id=1, word_id=3)
    listword_4 = ListWord(list_id=2, word_id=3)

    listword_5 = ListWord(list_id=3, word_id=4)
    listword_6 = ListWord(list_id=3, word_id=5)

    listword_7 = ListWord(list_id=4, word_id=6)

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

