from project.database.model import db, UserORM, UserStatus
import bcrypt


class User:
    def __init__(self, id, username, email, status, tier):
        self.id = str(id)
        self.username = username
        self.email = email
        self.status = status
        self.tier = tier
        self.is_authenticated = False

    def get_id(self) -> str:
        return self.id

    @property
    def is_active(self):
        if self.status == UserStatus.active:
            return True
        return False

    @property
    def is_anonymous(self):
        return False


def get_user_by_username(username) -> User:
    u = UserORM.query.filter(UserORM.username == username).first()
    return User(u.id, u.username, u.email, u.status, u.tier)


def get_user_by_id(id) -> User:
    u = UserORM.query.filter(UserORM.id == id).first()
    return User(u.id, u.username, u.email, u.status, u.tier)


def get_user_by_email(email) -> User:
    pass


def get_password_by_id(id):
    u = db.session.query(UserORM.password).filter(UserORM.id == id).first()
    return u


def get_password_hash(password) -> str:
    pwd_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
    string_password = hashed_password.decode("utf8")
    return string_password


def new_user(username, email, password):
    new_user = UserORM(username=username, password=password, email=email)
    db.session.add(new_user)
    db.session.commit()
    return UserORM.query.filter(UserORM.username == username).first()


def normalize_username(raw_username):
    return raw_username.lower().strip()


def normalize_email(raw_email):
    return raw_email.lower().strip()


def validate_email(email):
    errors = []
    if email == "":
        errors.append("Email cannot be empty")

    return errors


# Admin functions


def get_all_users():
    return UserORM.query
