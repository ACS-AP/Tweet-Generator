import sys
import random

words_list = sys.argv[1:]

def randomize_words():
  random.shuffle(words_list)
  return words_list



if __name__ == '__main__':
  words_randomized = randomize_words()
  print(' '.join(words_randomized))