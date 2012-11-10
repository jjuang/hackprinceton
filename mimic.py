#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys
import re
import os

#this is the part where you put in a word and get the word after
def function(word,filename):
	f=""
	f = open(filename, 'r')
	contents=f.read()
	#print word
	#print f
	#match= re.search(word,contents)
	#print match
	searchstr=word+'\s(\w+)[\W\s]'
	match2=re.search(searchstr,contents)
	if match2:
		returnstr=match2.group()
		answerstr=returnstr.replace(word,"")
		return answerstr
	else:
		print "sad"
#putting words and the next words into a dictionary
def mimic_dict(filename):
	with open (filename, 'r') as file:
		dict={}
  		for line in file:
			print line
     			for word in line.split():
				print word
				dict={word:function(word,filename)}	
				#return dict[word]

#this is the part that isnt working yet. this is supposed to be the part where you start with a word, which returns another word, etc
def print_mimic(startword,filename):
	print "hello"
	x= dict [startword]
  	print x
	"""for x in filename:
		x=dict[x]
		print x
"""
print_mimic("passengers","/home/jeanjuang/Desktop/gutenberg.txt")

#this was the default code, no idea what is going on.
# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print 'usage: ./mimic.py file-to-read'
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()
