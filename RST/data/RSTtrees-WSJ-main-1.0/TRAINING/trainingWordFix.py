import nltk, re, pprint, operator, sys, os, fnmatch, fileinput
from nltk import word_tokenize
from timeit import default_timer as timer

os.chdir('C:/Users/student/Dropbox/2016_05_RST/pRST/hash')
trainDict = open('word.lst').readlines()

i = 0
for i in range(0,5):
    print(trainDict[i])
    i+=1

count = 0
for w in trainDict:
    if w == None:
        print('count: ', count)

if count == 0:
    print('No null values found.')
        
