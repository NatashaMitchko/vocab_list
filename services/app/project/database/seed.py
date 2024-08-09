import csv
from random import random

from faker import Faker

from project.database.model import *
from project.database.user import get_password_hash


def _create_all():
    db.drop_all()
    db.create_all()
    db.session.commit()

def generate_users(n):
    faker = Faker()
    """Generate fake users."""
    for _ in range(n):
        user = UserORM(
            name=faker.name(),
            email=faker.email(),
            password=get_password_hash(faker.password()),
            status=UserStatus.active,
            tier=UserTier.admin
        )
        db.session.add(user)
    db.session.commit()

def generate_books(n):
    faker = Faker()
    for _ in range(n):
        book = BookORM(
            title=faker.sentence(nb_words=4, variable_nb_words=True).title(),
            author=faker.name,
            isbn=faker.isbn10
        )
        db.session.add(book)
    db.session.commit()


def extract_vocab(desired_num_results):
    vocab_list = "/Users/natashamitchko/src/vocab_list/services/vocab_csv_dev/words.csv"
    with open(vocab_list, 'r') as fp:
        total_entries = len(fp.readlines()) - 1

    chances_selected = desired_num_results / total_entries

    result = []
    for line in csv.reader(vocab_list):
        if random() < chances_selected:
            result.append((line[0], line[8], line[9]))
            if len(result) == desired_num_results:
                return result
    
def generate_words(n):
    words = extract_vocab(n)
    for w in words:
        db.session.add(WordORM(
            word=w[0],
            part_of_speech=w[1],
            definition_primary=w[2]
        ))
    db.session.commit()


def _seed_all():
    test_pw = get_password_hash("test")
    user_1 = UserORM(
        username="Natasha",
        status=UserStatus.active,
        tier=UserTier.admin,
        password=test_pw,
        email="a@b.com",
    )
    db.session.add(user_1)
    db.session.commit()

    generate_users(10)
    generate_books(50)
    generate_words(100)


    # Relations
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

    db.session.add_all(
        [
            list_1,
            list_2,
            list_3,
            list_4,
        ]
    )
    db.session.commit()

    db.session.add_all(
        [
            listword_1,
            listword_2,
            listword_3,
            listword_4,
            listword_5,
            listword_6,
            listword_7,
        ]
    )
    db.session.commit()
