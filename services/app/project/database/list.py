from typing import List

class Word:
    def __init__(self, id, word, part_of_speech, definition_primary, definition_secondary) -> None:
        self.id = id
        self.word = word
        self.part_of_speech = part_of_speech
        self.definition_primary = definition_primary
        self.definition_secondary = definition_secondary


class VocabList:
    def __init__(self, id: int, user_id: int, words: List[Word] = [], title = None, book_id = None) -> None:
        self.id = id
        self.user_id = user_id
        self.title = title
        self.book_id = book_id
        self.num_words = 0

        self.has_detail = False

        if words:
            self.has_detail = True
            self.num_words = len(words)
        self.words = words

