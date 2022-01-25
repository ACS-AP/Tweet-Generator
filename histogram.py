import sys

def histogram(source_text):
  dictionary = {}
  for word in source_text:
    if word in dictionary.keys():
      dictionary[word] += 1 
    else:
      dictionary[word] = 1
  return dictionary

def unique_words(source_text):
  dictionary = histogram(source_text)
  print(str(len(dictionary)))

def word_frequency(word, source_text):
  dictionary = histogram(source_text)
  if dictionary[word]:
    if dictionary[word] > 1:
      print("[" + str(dictionary[word]) + "] instances of " + str(word) +" unique words in the text.")
    else: 
      print("There is [" + str(dictionary[word]) + "] instances of " + str(word) +" unique words in the text.")
  else:
    print("Not found")

if __name__ == '__main__':
  file_name = sys.argv[1]
  word_check = sys.argv[2]
  f = open(file_name,'r', encoding='utf-8-sig')
  blog_text = f.read()
  clean_text = blog_text.replace(',','').replace('.','').replace('?','').replace("'",'').replace('"','').replace('-','')
  source_text = clean_text.split(' ')
  f.close()
  histogram(source_text)
  unique_words(source_text)
  word_frequency(word_check, source_text)

