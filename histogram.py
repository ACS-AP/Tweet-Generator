import sys

def histogramDict(word_text):
  dictionary = {}
  for word in word_text:
    if word in dictionary.keys():
      dictionary[word] += 1 
    else:
      dictionary[word] = 1
  return dictionary

def histogramList(word_text):
  word_list = []
  for word in word_text:
    for record in word_list:
      if record[0] == word:
        record[1] = record[1] + 1
    else:
      new_record = []
      new_record.append(word)
      new_record.append(1)
      word_list.append(new_record)
  print(word_list)
 
def uniqueWords(word_text):
  dictionary = histogramDict(word_text)
  print("There are " + str(len(dictionary)) + " in the text.")

def wordFrequency(word, word_text):

  dictionary = histogramDict(word_text)
  if dictionary[word]:
    if dictionary[word] > 1:
      print("There are " + str(dictionary[word]) + " instances of " + str(word) +" in the text.")
    else: 
      print("There is " + str(dictionary[word]) + " instances of " + str(word) +" in the text.")
  else:
    print("Not Found")



if __name__ == '__main__':
  file_name = sys.argv[1]
  word_check = sys.argv[2]
  f = open(file_name,'r', encoding='utf-8-sig')
  blog_text = f.read()
  clean_text = blog_text.replace(',','').replace('.','').replace('?','').replace("'",'').replace('"','').replace('-','')
  word_text = clean_text.split(' ')
  f.close()
  histogramDict(word_text)
  histogramList(word_text)
  uniqueWords(word_text)
  wordFrequency(word_check, word_text)

