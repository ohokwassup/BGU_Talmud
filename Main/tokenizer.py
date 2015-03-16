#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division  # Python 2 users only
import nltk, re, pprint
from nltk import word_tokenize
import codecs
import matplotlib.pyplot 
"""
Raphael Halff
March 14 2015
Attempt to tokenize excerpt of Talmud using NLTK
"""

path = '/Users/Raphi/Documents/WorkThings/Talmud Pro/Main/mishna_ex.txt'
f = codecs.open(path, encoding='utf8')
"""for line in f:
    line = line.strip()
    print(line)"""
raw = f.read()
print 'READING TEXT:\n'
print raw
tokens = word_tokenize(raw)
fdist = nltk.FreqDist(tokens)
sorted(fdist)
for key in fdist:
    print key.encode('utf8') + ':' + str(fdist[key]) + ';\n'
fdist.plot()

