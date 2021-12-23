#Author: Arshveer Gahir


#!/usr/bin/env python3
def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  pig_sentence = []
  for word in words:
    # Create the pig latin word and add it to the list
    delim = " "
    first_word = word[0]
    word_body = word[1:]
    pig_word = word_body + first_word + "ay"
    pig_sentence.append(pig_word)

    # Turn the list back into a phrase
  print(delim.join(pig_sentence))

def main():
  phrase = str(input('Enter a phrase to be converted to Pig Latin: '))
  pig_latin(phrase)


if __name__ == "__main__":
  main()
  



#pig_latin("hello how are you") #
#  Result =  Should be "ellohay owhay reaay ouyay"

#pig_latin("programming in python is fun") 
#   Result = Should be "rogrammingpay niay ythonpay siay unfay"
