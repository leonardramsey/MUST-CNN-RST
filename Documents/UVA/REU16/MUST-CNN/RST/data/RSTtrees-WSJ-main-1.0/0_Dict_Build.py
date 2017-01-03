#### RST Preprocessing
#### Leonard Ramsey, 7.13.16
#### Dr. Yanjun Qi, MLDM Lab, Rice 228, REU 2016
#### RST: 458,790 non-unique words
#### 178,825 tokens
##
import nltk, re, pprint, operator, sys, os, fnmatch, fileinput
#### from nltk.book() import *
#### text7 ^ is the Wall Street Journal (WSJ) also used in RST
from nltk import FreqDist
from nltk import word_tokenize
from timeit import default_timer as timer

## loop through all files in RST, compile text to one file for parsing
## already completed task, code below commented out for future runs

## with open('RST_Compilation.txt', 'a') as newFile:
##    for fn in os.listdir('.'):
##        if fnmatch.fnmatch(fn, '*.out'):
##            tempFile = open(fn).read()
##            newFile.write(tempFile)

## preprocessing; X = dictionary hash; Y = class hash
## fileToParse = open('wsj_2399.out').read()
fileToParse = open('RST_ALL_EDUs.txt').read()

## X = hash dictionary of tokens from RST texts

X = {}
## set 1st element, pad, to max int value for ordering hash later on
X['PADDING'] = sys.maxsize 
print('X Hash prior to additions from text: ', X)
print('Total size of hash of tokens: ', len(word_tokenize(fileToParse)))

## add word types from text to X Hash (Dictionary) with frequencies as values
## freq() returns frequency of a sample, defined as
## sample count / total # sample outcomes recorded by freqdist
## N() returns total number of sample outcomes recorded by freqdist
## freq()*N() yields sample count

count = 0
totalTime = 0
freqdist = FreqDist(word_tokenize(fileToParse))
start = timer()

for w in word_tokenize(fileToParse):
    worig = w
    w = w.lower()
    w = re.sub('\W+','',w)
    if re.match('\d+',w)!=None:
        w = '#NUM'
    if w!='':
        if not w in X:
            X[w] = int(freqdist.freq(worig)*freqdist.N())
        else:
            X[w] = X[w] + int(freqdist.freq(worig)*freqdist.N())
        count = count + 1

end = timer()
buildTime = end - start
buildTimeMin = int(buildTime / 60)
buildTimeSec = buildTime - (buildTimeMin * 60)
print('Time taken to build dictionary: ', buildTimeMin, ' minutes, ', buildTimeSec, ' s.')
 
###### sort hash dictionary into set (list) in descending order by frequency
sorted_X = sorted(X.items(), key=operator.itemgetter(1), reverse=True)
print('X Dictionary sorted.')

## add X hash to one text file for viewing
## already completed task, code below commented out for future runs

##with open('RST_Dict.dat', 'a') as newFile:
##   newFile.write(str(sorted_X))

with open('word.lst', 'w') as newFile:
   for x in range(0, len(sorted_X)):
       w = list(sorted_X[x])[0]
       newFile.write(str(w))
       newFile.write('\n')


