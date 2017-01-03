import nltk, re, pprint, operator, sys, os, fnmatch, fileinput
from nltk import FreqDist
from nltk import word_tokenize
from timeit import default_timer as timer

with open('RST_TEST_EDU_Line_By_Line_Lowercase.txt', 'a') as newFile:
   for fn in os.listdir('.'):
       if fnmatch.fnmatch(fn, '*.out.edus'):
           tempFile = open(fn)
           lines = tempFile.readlines()
           article = ' '.join([line.lower().strip() for line in lines])
           newFile.write(article)
           newFile.write('\n')

