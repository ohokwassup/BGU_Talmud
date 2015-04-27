#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division  # Python 2 users only
import nltk, re, pprint
from nltk import tokenize, word_tokenize, probability
from nltk.text import ConcordanceIndex 
from nltk.tokenize import RegexpTokenizer
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

if not os.path.exists('/Users/Raphi/Documents/WorkThings/Talmud_Pro/Main/tokens.pkl'):
    #making the pickled file of tokens, will use the tokens.pkl file if one is present
    path = '/Users/Raphi/Documents/WorkThings/Talmud_Pro/Main/talmud.txt' # or mishna_ex.txt for testing

    #f = codecs.open(path, encoding='utf8')

    """for line in f:
        line = line.strip()
        print(line)"""
    tokenizer = RegexpTokenizer("""(\S+"\S+)|\s?[\u05D0-\u05EA]+\s|(\.|\\|\?|\(|\)|:|;)|([\u05D0-\u05EA]'\s)""")
    def make_tokens():
        with codecs.open(path, encoding='utf8') as f:
            for line in f:
                #for word in line.split():
                yield tokenizer.tokenize(line) #word_tokenize(line) #tokenize or word_tokenize?
    #storing as freqdist
    tokens = []
    tokens = make_tokens()
    tokenslist = []
    #print 'printing tokens'
    #print tokens
    #print 'printing t in tokens'
    count = 0
    for t in tokens:
        if type(t) is list:
            for tks in t:
                #print tks.encode('utf8')
                tokenslist.append(tks)
                count = count + 1
            #tokens = t
        else:#this wont happen, tokenizer is returning list of tokens by line, every line is a list
            tokenslist.append(t)
            count = count + 1
    print str(count) + ' tokens'
    fdist = nltk.FreqDist(tokenslist)
    print fdist.N() #print how many outcomes
    sorted(fdist)
    print fdist.max()
    #fdist.plot(10)#add integer to limit number of items plotted
    #attempt to store tokens directly from generator to freqdist
    """ 
    fdist = nltk.FreqDist(make_tokens())
    sorted(fdist)
    """
    #printing tokens
    """
    for key in fdist:
        print key.encode('utf8') + ': ' + str(fdist[key]) + '; ',
    """
    #pickling
    outfile_tokens = open("tokens.pkl", "wb")
    outfile_dist = open("dist.pkl","wb")
    pickle.dump(tokenslist, outfile_tokens, 1)
    pickle.dump(fdist, outfile_dist, 1) #MUST use protocol 1, else 'FreqDist'[...]'_N' error, might be interesting to know why 
    outfile_tokens.close()
    outfile_dist.close()
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
#pickle file made, begin here if pickled file already existed
#test unpickling
print 'STARTING ON THE PICKLED FILES'
infile_tokens = open("tokens.pkl", "rb")
tokens = pickle.load(infile_tokens)
infile_tokens.close()
print 'TOKENS HAVE BEEN LOADED'

infile_dist = open("dist.pkl", "rb")
dist = pickle.load(infile_dist)
infile_dist.close()
print 'DISTRIBUTIONS HAVE BEEN LOADED'

print 'number of hapaxes: ' +  str(len(dist.hapaxes()))
print str(dist.N()) + ' outcomes' #print how many outcomes
sorted(dist)
cindex = ConcordanceIndex(dist.samples())
cindex.print_concordance('"')
dist.plot(10)#add integer to limit number of items plotted
