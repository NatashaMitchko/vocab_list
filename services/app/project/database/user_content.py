from project.database.model import db, ListORM, WordORM, ListWordORM
from project.database.list import VocabList, Word
from typing import List
from sqlalchemy import func


def get_lists_for_user(user_id) -> List[VocabList]:
    """
    Join on Book to do something with book title
    """
    lists = (
        db.session.query(ListORM, func.count(ListWordORM.id))
        .join(ListWordORM.list)
        .group_by(ListORM.id)
        .filter(ListORM.user_id == user_id)
        .all()
    )
    result = []
    for l, c in lists:
        result.append(
            VocabList(
                id=l.id, user_id=l.user_id, title=l.title, book_id=l.book_id, count=c
            )
        )
    return result


def get_list_detail(list_id) -> VocabList:
    # after calling make sure user_id matches current user or perms
    db_list = (
        db.session.query(ListORM, WordORM)
        .select_from(WordORM)
        .join(ListWordORM, ListWordORM.word_id == WordORM.id)
        .join(ListORM, ListORM.id == ListWordORM.list_id)
        .filter(ListORM.id == list_id)
        .filter(ListWordORM.list_id == list_id)
        .all()
    )
    words = []
    vl = None
    for l, w in db_list:
        vl = l
        words.append(
            Word(
                w.id,
                w.word,
                w.part_of_speech,
                w.definition_primary,
                w.definition_secondary,
            )
        )
    return VocabList(vl.id, vl.user_id, words=words, title=vl.title, book_id=vl.book_id)
