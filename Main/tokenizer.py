#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division  # Python 2 users only
import nltk, re, pprint
from nltk import tokenize, word_tokenize, probability
import codecs
from pylab import *
import sys
import os.path
import pickle

"""
Raphael Halff
March 14 2015
Attempt to tokenize excerpt of Talmud using NLTK
"""


path=""
to_print = True
if len(sys.argv)==3:
    if os.path.exists(sys.argv[1]):
        path = sys.argv[1]
        if sys.argv[2].lower()=="n":
            to_print = False
    else:
        print "usage: python tokenizer.py [/path/|d=default] [print output?: y|n]" #what is the proper usage notation?
elif len(sys.argv)==2:
    if os.path.exists(sys.argv[1]):
        path = sys.argv[1]
    else:
        print "usage: python tokenizer.py [/path/|d=default]" #what is the proper usage notation?
else:
    if not os.path.exists('/Users/Raphi/Documents/WorkThings/Talmud_Pro/Main/tokens.pkl'):
        path = '/Users/Raphi/Documents/WorkThings/Talmud_Pro/Main/talmud.txt' # or mishna_ex.txt for testing

        #f = codecs.open(path, encoding='utf8')

        """for line in f:
            line = line.strip()
            print(line)"""
        def make_tokens():
            with codecs.open(path, encoding='utf8') as f:
                for line in f:
                    #for word in line.split():
                    yield word_tokenize(line) #tokenize or word_tokenize?
        #storing as freqdist
        tokens = []
        tokens = make_tokens()
        print 'printing tokens'
        print tokens
        print 'printing t in tokens'
        for t in tokens:
            if type(t) is list:
                print 'tks are coming'
                for tks in t:
                    print tks.encode('utf8')
                tokens = t
        fdist = nltk.FreqDist(tokens)
        print fdist.N() #print how many outcomes
        sorted(fdist)
        #fdist.plot(10)#add integer to limit number of items plotted
        #attempt to store tokens directly from generator to freqdist
     """fdist = nltk.FreqDist(make_tokens())
        sorted(fdist)
        """
        #printing tokens
    """ for key in fdist:
            print key.encode('utf8') + ': ' + str(fdist[key]) + '; ',
        """
        #pickling
        outfile = open("tokens.pkl","wb")
        pickle.dump(fdist, outfile, 1) #MUST use protocol 1, else 'FreqDist'[...]'_N' error, might be interesting to know why 
        outfile.close()

        #test unpickling
        infile = open("tokens.pkl", "rb")
        dist = pickle.load(infile)
        infile.close()
        #dist.plot()
        """
        raw = f.read()
        if to_print:
            print 'Raw Text:\n'
            print raw
        """
        #tokens = word_tokenize(raw)
        """
        fdist = nltk.FreqDist(tokens)
        sorted(fdist)


        if to_print:
            print '\nTokens:\n'
            for key in fdist:
                print key.encode('utf8') + ': ' + str(fdist[key]) + '; ',
            print '\n\nUnique words: \n' 
            for w in  fdist.hapaxes():
                print w.encode('utf8') + '; ',

        print '\n\nPlotting...' #would like to switch y and x axis
        fdist.plot(title='Tokenization: Word Frequency')
        """

#test unpickling
print 'STARTING THE UNPICKLED FILE'
infile = open("tokens.pkl", "rb")
dist = pickle.load(infile)
infile.close()
print dist.N() #print how many outcomes
sorted(dist)
dist.plot(10)#add integer to limit number of items plotted
