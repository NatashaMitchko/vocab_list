from project.database.model import db, ListORM, WordORM, ListWordORM
from project.database.list import VocabList, Word
from typing import List


def get_lists_for_user(user_id) -> List[VocabList]:
    """
    Join on Book to do something with book title
    """
    lists = db.session.query(ListORM).filter(ListORM.user_id == user_id).all()
    result = []
    for l in lists:
        result.append(VocabList(l.id, l.user_id, l.title, l.book_id))
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
