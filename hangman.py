import linecache
import random


rand_num = random.randint(0, 370099)
word_to_guess = linecache.getline('words_alpha.txt', rand_num)
print(word_to_guess)
