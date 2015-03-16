"""
Raphael Halff
3.3.2015
Tokenizer gathers unique words from file and counts their frequency
"""

import codecs

class Token(object):
	def __init__(self, name, loc):
		self.name = name
		self.count = 1 
		self.locs = [loc]
		
	def log(location):
		self.count += 1
		self.locs.append(location)

file = codecs.open("talmud.txt", "r", encoding="UTF-8")
talmud = file.read()
file.close()

tokens = []

def find(word):
	for t in tokens:
		if t.name == word:
			return index(t)
	
		
#here go through talmud whitespace to whitespace, if word is not in tokens list, add it, otherwise log existing token