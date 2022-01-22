import random
import sys

def read_words():
  with open("/usr/share/dict/words") as words_file:
    words = words_file.readlines()
    return words

def print_random(words, num_print):
  select_words = random.choices(words, k = num_print)
  for word in [line.strip("\n") for line in select_words]:
    print(word, end=" ")

if __name__ == "__main__":
  words = read_words()
  print_random(words, int(sys.argv[1]))

