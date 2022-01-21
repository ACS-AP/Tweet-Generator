import sys
import random

num_words = int(sys.argv[1:][0])

f = open('words.txt', 'r')
words = f.read()
words_list = words.split(" ")

def randomize_file_words():
  random.shuffle(words_list)
  return words_list

if __name__ == '__main__':
  shuffled_words = randomize_file_words()
  print(' '.join(shuffled_words[0:num_words]))