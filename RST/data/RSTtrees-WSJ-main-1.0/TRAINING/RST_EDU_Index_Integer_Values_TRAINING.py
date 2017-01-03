import nltk, re, pprint, operator, sys, os, fnmatch, fileinput

Y = []
count = 0
for i in range(0,18765): ## 18764 EDUs
    Y.append(i)
with open('RST_EDU_Output.dat', 'a') as newFile:
   newFile.write(str(Y))
