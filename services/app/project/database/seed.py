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
            username=faker.name(),
            email=faker.email(),
            password=get_password_hash(faker.password()),
            status=UserStatus.active,
            tier=UserTier.admin,
        )
        db.session.add(user)
    db.session.commit()


def generate_books(n):
    faker = Faker()
    for _ in range(n):
        book = BookORM(
            title=faker.sentence(nb_words=4, variable_nb_words=True).title(),
            author=faker.name(),
            isbn=faker.isbn10(),
        )
        db.session.add(book)
    db.session.commit()


vocab_sample = [
    (
        "tyranny",
        "noun",
        "a form of government in which the ruler is an absolute dictator (not restricted by a constitution or laws or opposition etc.)",
    ),
    ("sublime", "adjective", "inspiring awe"),
    ("ruffian", "noun", "a cruel and brutal fellow"),
    ("astute", "adjective", "marked by practical hardheaded intelligence"),
    ("criteria", "noun", "Plural form of criterion#English|criterion|lang=English"),
    ("comport", "verb", "behave in a certain manner"),
    (
        "breviary",
        "noun",
        "(Roman Catholic Church) a book of prayers to be recited daily certain priests and members of religious orders",
    ),
    (
        "effigy",
        "noun",
        "a representation of a person (especially in the form of sculpture)",
    ),
    ("dejected", "adjective", "affected or marked by low spirits"),
    ("agglomerate", "adjective", "clustered together but not coherent"),
    (
        "allegiance",
        "noun",
        "the act of binding yourself (intellectually or emotionally) to a course of action",
    ),
    ("select", "verb", "pick out, select, or choose from a number of alternatives"),
    ("proffer", "verb", "present for acceptance or rejection"),
    ("resignation", "noun", "acceptance of despair"),
    ("outstanding", "adjective", "of major significance or importance"),
    (
        "sherbet",
        "noun",
        "a frozen dessert made primarily of fruit juice and sugar, but also containing milk or egg-white or gelatin",
    ),
    ("afire", "adjective", "lighted up by or as by fire or flame"),
    ("doting", "adjective", "extravagantly or foolishly loving and indulgent"),
    (
        "discombobulated",
        "adjective",
        "having self-possession upset; thrown into confusion",
    ),
    ("caparison", "verb", "put a caparison on"),
    (
        "nettle",
        "noun",
        "any of numerous plants having stinging hairs that cause skin irritation on contact (especially of the genus Urtica or family Urticaceae)",
    ),
    ("discharge", "verb", "complete or carry out"),
    ("coquette", "noun", "a seductive woman who uses her sex appeal to exploit men"),
    (
        "necrology",
        "noun",
        "a notice of someone's death; usually includes a short biography",
    ),
    ("irrefutable", "adjective", "impossible to deny or disprove"),
    ("smolder", "noun", "a fire that burns with thick smoke but no flame"),
    ("impinge", "verb", "advance beyond the usual limit"),
    ("levy", "verb", "To impose or collect (a tax, for example)."),
    (
        "renunciation",
        "noun",
        "the act of renouncing; sacrificing or giving up or surrendering (a possession or right or title or privilege etc.)",
    ),
    ("turn down", "verb", "To refuse, decline, or deny."),
    ("stringent", "adjective", "demanding strict attention to rules and procedures"),
    ("delude", "verb", "be false to; be dishonest with"),
    ("exaction", "noun", "act of demanding or levying by force or authority"),
    ("subjugate", "verb", "put down by force or intimidation"),
    ("skinflint", "noun", "a selfish person who is unwilling to give or spend"),
    ("effervesce", "verb", "become bubbly or frothy or foaming"),
    ("plumb", "verb", "weight with lead"),
    ("subsistence", "noun", "minimal (or marginal) resources for subsisting"),
    ("sham", "verb", "make believe with the intent to deceive"),
    (
        "hauteur",
        "noun",
        "overbearing pride evidenced by a superior manner toward inferiors",
    ),
    ("disqualify", "verb", "make unfit or unsuitable"),
    ("reverberate", "verb", "have a long or continuing effect"),
    ("submerge", "verb", "sink below the surface; go under or as if under water"),
    (
        "hoax",
        "noun",
        "something intended to deceive; deliberate trickery intended to gain an advantage",
    ),
    (
        "conjugal",
        "adjective",
        "of or relating to marriage or to the relationship between a wife and husband",
    ),
    ("circumscribe", "verb", "restrict or confine"),
    ("fissure", "noun", "a long narrow opening"),
    ("bellicose", "adjective", "having or showing a ready disposition to fight"),
    (
        "hypertension",
        "noun",
        "a common disorder in which blood pressure remains abnormally high (a reading of 140/90 mm Hg or greater)",
    ),
    ("dissonance", "noun", "a conflict of people's opinions or actions or characters"),
]


def generate_words(n):
    for w in vocab_sample:
        db.session.add(WordORM(word=w[0], part_of_speech=w[1], definition_primary=w[2]))
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
