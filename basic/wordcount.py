#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys
import string

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###
# reads a file and return a dict of (words, count) in lower case
def read_file(filename):
  word_cnt_d = {}
  fd = open(filename, "r")

  for line in fd:
    #print (line)
    line = line.strip('\n')
    if len(line) > 0 : # work on none empty lines only
      #line = line.translate(str.maketrans({"(" : None, ")" : None}))
      line = line.translate(str.maketrans("--", "  "))
      line = line.translate(str.maketrans("","",string.punctuation))
      words = line.split()

      #print(words)
      for word in words :
        word_l = word.lower()
        if word_l not in word_cnt_d :
          word_cnt_d[word_l] = 1
        else :
          word_cnt_d[word_l] += 1

  #print (word_cnt_d)

  #sys.exit(0)
  return word_cnt_d

#
def print_words(filename):
  word_cnt_d = read_file(filename)
  for key in sorted(word_cnt_d.keys()) :
    print (key, word_cnt_d[key])
  return

#
def get_value(apair):
  return apair[1]

def print_top(filename):
  word_cnt_d = read_file(filename)
  word_cnt_d_new = {}
  cnt = 0
  for k, v in word_cnt_d.items() :
    word_cnt_d_new[v] = k

  for key in sorted(word_cnt_d_new.keys(), reverse=True) :
    #print (word_cnt_d_new[key], key)
    cnt +=1
    if cnt == 20 : break

  #preferable answer
  items = sorted(word_cnt_d.items(), key=get_value, reverse=True)
  for item in items[:20] :
    print (item[0], item[1])

  return

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print ('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print ('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
