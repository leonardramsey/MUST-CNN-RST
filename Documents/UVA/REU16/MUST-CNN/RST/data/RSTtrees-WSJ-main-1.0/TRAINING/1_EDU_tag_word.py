#!/usr/bin/python

import nltk, re, pprint, operator, sys, os, fnmatch, fileinput
from nltk import word_tokenize
from timeit import default_timer as timer

if len(sys.argv) <= 3:
    print 'command hashdir outdir datadir'

print 'Number of arguments:', len(sys.argv), 'arguments.'

hashdir = str(sys.argv[1])
outdir = str(sys.argv[2])
datadir = str(sys.argv[3])
print 'hashdir:', hashdir
print 'outdir:', outdir
print 'datadir:', datadir

## change dir to whereever dict is
#hashdir = 'C:/Users/student/Dropbox/2016_05_RST/pRST/hash/'
#outdir = 'C:/Users/student/Dropbox/2016_05_RST/pRST/train/'
#outdir = 'C:/Users/student/Dropbox/2016_05_RST/pRST/test/'
## change dir to whereever EDU Files are
#os.chdir('C:/Users/student/Documents/UVA/REU 16/MUST-CNN/RST/data/RSTtrees-WSJ-main-1.0/TRAINING')
#os.chdir('C:/Users/student/Documents/UVA/REU 16/MUST-CNN/RST/data/RSTtrees-WSJ-main-1.0/TEST')

#dict = set(open('word.lst').read().splitlines())
input_file = open(hashdir+'word.lst', 'r')

dict = {}
count_lines = 0
for line in input_file:
    word = line.strip()
    dict[word]= count_lines
    count_lines += 1
    ## print(word, " ", count_lines)
##print('number of lines:', count_lines)
print('Length of word dict: ', len(dict))


##edu_hash['B'] = 1 ## beginning of EDU
##edu_hash['E'] = 2 ## ending of EDU
##edu_hash['N'] = 3 ## no break in EDU

count = 0
finalFile = open(outdir+'rst.tag.dat', 'w')
finalFile2 = open(outdir+'word.dat', 'w')

countl = 0
## iterates through each file in the same directory as this program
for fn in os.listdir(datadir):
    ## checks to see if a file has the below extension
    if fnmatch.fnmatch(fn, datadir+'*.out.edus'):
        ## if it does, opens the file and stores it in a local variable
        tempFile = open(fn)
        ## creates a list of every line in the file
        lines = tempFile.readlines()
        ## creates a list of every token in every line
        for line in lines:
            line.lower().strip()
            ## retrieve list of tokens from current line
            tokens = word_tokenize(line)
            ## for each token in the current line, tag
            for w in range(0, len(tokens)):
                tokens[w] = tokens[w].lower()
                tokens[w] = re.sub('\W+','',tokens[w])
                if re.match('\d+',tokens[w])!=None:
                    tokens[w] = '#NUM'
                if tokens[w] =='':    
                     continue

                outtag = ""
                if w == 0:
                    outtag = '1'
                elif w == len(tokens)-1:
                    outtag = '2'
                else:
                    outtag = '3'
                finalFile.write(str(outtag)+' ')
                count += 1

                finalFile2.write(str(dict.get(tokens[w])))
                finalFile2.write(" ")

        finalFile2.write('\n')
        finalFile.write('\n')
        count += 1
    countl +=1 

print('Total token: ', count, '; Total line: ',countl)


