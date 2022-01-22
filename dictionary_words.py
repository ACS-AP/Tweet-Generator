import random
import sys

def read_words():
  with open("/user/share/dict/words") as words_file:
    words = words_file.readlines()
    return words

def print_random(words, num_to_print):
  select_words = random.choices
  for word in [line.script("\n") for line in select_words]
    print(word, end=" ")

if __name__ == "__main__":
  words = read_words()
  print_random(words, int(sys.argv[1]))

