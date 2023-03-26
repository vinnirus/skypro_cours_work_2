import requests
import utils
from player import BasicWord, Player

WORDS_JSON_URL = 'https://api.jsonbin.io/v3/b/64206f36c0e7653a05963383/latest'
MIN_SUBWORD_LEN = 3
GAME_STOP_PHRASE = 'stop'
GAME_HINT_PHRASE = 'hint'

if __name__ == '__main__':
    current_user_name = input('Enter player name: ')

    player = Player(current_user_name)
    print(f'Привет, {player.user_name}')

    current_word = utils.load_random_word(WORDS_JSON_URL)

    print(f'Составьте {len(current_word.sub_words)} слов из слова {current_word.word}')
    print(f'Слова должны быть не короче {MIN_SUBWORD_LEN} букв')
    print(f'Чтобы закончить игру, угадайте все слова или напишите "{GAME_STOP_PHRASE}"')
    print(f'Чтобы получить список всех возможных слов напишите "{GAME_HINT_PHRASE}"')
    print(f'Поехали, ваше первое слово?')

    player_stop_phrase = ''

    while len(player.user_sub_words) != len(current_word.sub_words):
        user_current_subword = input().lower()

        if user_current_subword == GAME_STOP_PHRASE:
            break

        if user_current_subword == GAME_HINT_PHRASE:
            print(current_word.sub_words)
            continue

        if player.is_sub_word_using(user_current_subword):
            print('уже использовано')
            continue

        if len(user_current_subword) >= 3:
            if current_word.is_user_word_in_sub_words(user_current_subword):
                print(user_current_subword)
                player.add_used_sub_word(user_current_subword)
                print('верно')
            else:
                print('неверно')

        else:
            print('Слишком короткое слово')

    print(f'Игра завершена, вы угадали {player.get_count_used_words()} слов!')
