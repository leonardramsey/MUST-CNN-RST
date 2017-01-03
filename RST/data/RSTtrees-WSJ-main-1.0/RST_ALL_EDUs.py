import nltk, re, pprint, operator, sys, os, fnmatch, fileinput
from nltk import FreqDist
from nltk import word_tokenize
from timeit import default_timer as timer

trainEDUdir = 'C:/Users/student/Documents/UVA/REU 16/MUST-CNN/RST/data/RSTtrees-WSJ-main-1.0/TRAINING'
testEDUdir = 'C:/Users/student/Documents/UVA/REU 16/MUST-CNN/RST/data/RSTtrees-WSJ-main-1.0/TEST'
RSTdir = 'C:/Users/student/Documents/UVA/REU 16/MUST-CNN/RST/data/RSTtrees-WSJ-main-1.0'

os.chdir(trainEDUdir)
trainf = open('RST_ALL_EDUs.txt', 'w')
for fn in os.listdir('.'):
   if fnmatch.fnmatch(fn, '*.out.edus'):
       tempFile = open(fn)
       lines = tempFile.readlines()
       article = ' '.join([line.lower().strip() for line in lines])
       trainf.write(article)
       trainf.write('\n')

os.chdir(testEDUdir)
testf = open('RST_ALL_EDUs.txt', 'w+')
for fn in os.listdir('.'):
   if fnmatch.fnmatch(fn, '*.out.edus'):
       tempFile = open(fn)
       lines = tempFile.readlines()
       article = ' '.join([line.lower().strip() for line in lines])
       testf.write(article)
       testf.write('\n')

os.chdir(trainEDUdir)
trainf.write(testf.read())
