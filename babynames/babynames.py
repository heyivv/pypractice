#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++

  # Open file string
  f = open(filename, 'r')
  fstr = f.read()

  # Extract year
  match_year_s = re.findall(r'Popularity in (\d+)', fstr)
  #print ("YEAR matches")
  #for yr in match_year_s :
  # print (yr)

  final_str = [match_year_s[0]]

  # Extract baby names and ranking
  match_rank_name_t = re.findall(r'<.*?>(\d+)</.*?><.*?>(\w+?)</.*?><.*?>(\w+?)</.*?>', fstr)
  #print ("RANK NAME NAME matches")


  for rn_t in match_rank_name_t :
    #print (rn_t[0] + ' ' + rn_t[1] + ' ' + rn_t[2])
    final_str.append(rn_t[1]+' '+rn_t[0])
    final_str.append(rn_t[2]+' '+rn_t[0])
  #print ("FINAL_STR length = " + str(len(final_str)))

  #str[0] = yr
  final_str = sorted(final_str)
  #print (final_str)

  return final_str

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print ('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file

  # parse the file name
  for fname in args :
    print ('Reading file : ' + fname)
    result = extract_names(fname)
    if summary :
      outf = open(fname+'.summary', 'w')
      result_s = '\n'.join(str(s) for s in result)
      outf.write(result_s)
      outf.close()
    else :
      print (result)


if __name__ == '__main__':
  main()
