class BasicWord:

    def __init__(self, word: str, sub_words: []) -> None:
        self.word = word
        self.sub_words = sub_words

    def __repr__(self):
        return f"class BasicWord ({self.word}, {self.sub_words})"

    def is_user_word_in_sub_words(self, user_word: str) -> bool:
        return user_word in self.sub_words

    def count_sub_words(self) -> int:
        return len(self.sub_words)


class Player:

    def __init__(self, user_name: str, user_sub_words: list[str] = []) -> None:
        if user_sub_words is None:
            user_sub_words = []
        self.user_name = user_name
        self.user_sub_words = user_sub_words

    def __repr__(self):
        return f"class Player ({self.user_name},{self.user_sub_words})"

    def get_count_used_words(self) -> int:
        """
        :return: count used user sub words in basic sub words
        """
        return len(self.user_sub_words)

    def add_used_sub_word(self, new_user_sub_word: str) -> None:
        self.user_sub_words.append(new_user_sub_word)

    def is_sub_word_using(self, input_user_word: str) -> bool:
        return input_user_word in self.user_sub_words
