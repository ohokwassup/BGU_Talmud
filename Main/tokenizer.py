#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division  # Python 2 users only
import nltk, re, pprint
from nltk import word_tokenize, probability
import codecs
from pylab import *
import sys
import os.path


"""
Raphael Halff
March 14 2015
Attempt to tokenize excerpt of Talmud using NLTK
"""


path=""
if len(sys.argv)==2:
    if os.path.exists(sys.argv[1]):
        path = sys.argv[1]
    else:
        print "usage: python tokenizer.py [/path/|d=default]" #what is the proper usage notation?
else:
    path = '/Users/Raphi/Documents/WorkThings/Talmud_Pro/Main/mishna_ex.txt'

f = codecs.open(path, encoding='utf8')

"""for line in f:
    line = line.strip()
    print(line)"""

raw = f.read()
print 'Raw Text:\n'
print raw

tokens = word_tokenize(raw)
fdist = nltk.FreqDist(tokens)
sorted(fdist)

print '\nTokens:\n'
for key in fdist:
    print key.encode('utf8') + ': ' + str(fdist[key]) + '; ',
print '\n\nUnique words: \n' 
for w in  fdist.hapaxes():
    print w.encode('utf8') + '; ',

print '\n\nPlotting...' #would like to switch y and x axis
fdist.plot(title='Tokenization: Word Frequency')

