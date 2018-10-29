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
guessed = '-' * (len(word_to_guess) - 1)
num_mistakes = 0

while(num_mistakes < 8):
    print(guessed)
    guess = input('Guess another letter: ')[0]
    if guess in word_to_guess:
        for i in range(len(word_to_guess)):
            if guess == word_to_guess[i]:
                guessed = guessed[:i] + guess + guessed[i + 1:]
                if '-' not in guessed:
                    print('CONGRATULATIONS! You guessed the word ' + word_to_guess)
                    import sys
                    sys.exit()
    else:
        num_mistakes += 1
        print(draw_hangman(num_mistakes))

print('GAME OVER!\nword is ' + word_to_guess)
