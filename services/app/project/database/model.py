from project.app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    username = db.Column(db.String(128), unique=True, nullable=False)
    email_validated = db.Column(db.Boolean, nullable=False, default=False)


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=False, nullable=False)
    author = db.Column(db.String(128), unique=False, nullable=False)
    isbn = db.Column(db.String(128), unique=True, nullable=False)


class Word(db.Model):
    __tablename__ = 'words'

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(128), nullable=False)
    part_of_speech = db.Column(db.String(128), nullable=False)
    definition_primary = db.Column(db.String(128), nullable=False)
    definition_secondary = db.Column(db.String(128), nullable=True)


class List(db.Model):
    __tablename__ = 'lists'
    __table_args__ = (
        db.UniqueConstraint('user_id', 'book_id', 'list_title', postgresql_nulls_not_distinct=True),
      )

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=True)
    list_title = db.Column(db.String(128), nullable=True)


class ListWord(db.Model):
    __tablename__ = 'list_words'
    __table_args__ = (
        db.UniqueConstraint('list_id', 'word_id'),
      )

    id = db.Column(db.Integer, primary_key=True)
    list_id = db.Column(db.Integer, db.ForeignKey('lists.id'))
    word_id = db.Column(db.Integer, db.ForeignKey('words.id'))

    list = db.relationship('List', backref='list_words')
    word = db.relationship('Word', backref='list_words')

def _create_all():
    db.drop_all()
    db.create_all()
    db.session.commit()