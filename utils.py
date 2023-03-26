import requests
import random
import json

from player import BasicWord, Player


def load_random_word(url: str) -> BasicWord:
    req = requests.get(url)
    words_dict = json.loads(req.content)

    random_word = words_dict["record"][random.randint(0, len(words_dict))]
    return BasicWord(random_word["word"], random_word["subwords"])


