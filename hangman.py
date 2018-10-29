import linecache
import random


def draw_hangman(num_mistakes):
    hangman_drawing = {
        1: '_____\n' +
           '|    \n' +
           '|    \n' +
           '|    \n' +
           '|    \n' +
           '|    \n' +
           '|    \n',
        2: '_____\n' +
           '|    \n' +
           '|   O\n' +
           '|    \n' +
           '|    \n' +
           '|    \n' +
           '|    \n',
        3: '_____\n' +
           '|    \n' +
           '|   O\n' +
           '|   |\n' +
           '|    \n' +
           '|    \n' +
           '|    \n',
        4: '_____\n' +
           '|    \n' +
           '|   O\n' +
           '|  /|\n' +
           '|    \n' +
           '|    \n' +
           '|    \n',
        5: '_____\n' +
           '|    \n' +
           '|   O\n' +
           '|  /|\\\n' +
           '|    \n' +
           '|    \n' +
           '|    \n',
        6: '_____\n' +
           '|    \n' +
           '|   O\n' +
           '|  /|\\\n' +
           '|  / \n' +
           '|    \n' +
           '|    \n',
        7: '_____\n' +
           '|    \n' +
           '|   O\n' +
           '|  /|\\\n' +
           '|  / \\\n' +
           '|    \n' +
           '|    \n',
        8: '_____\n' +
           '|   |\n' +
           '|   O\n' +
           '|  /|\\\n' +
           '|  / \\\n' +
           '|    \n' +
           '|    \n'
    }
    return hangman_drawing.get(num_mistakes)

rand_num = random.randint(0, 370099)
word_to_guess = linecache.getline('words_alpha.txt', rand_num)

