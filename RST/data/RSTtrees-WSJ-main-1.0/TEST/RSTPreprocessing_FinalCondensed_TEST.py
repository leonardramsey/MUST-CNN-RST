import nltk, re, pprint, operator, sys, os, fnmatch, fileinput
from nltk import word_tokenize
from timeit import default_timer as timer

fileToParse = open('RST_TEST_EDUs.txt').read()

edu_hash = {}
## edu_hash['B'] = 1 ## beginning of EDU
## edu_hash['E'] = 2 ## ending of EDU
## edu_hash['N'] = 3 ## no break in EDU

count = 0

## opens the file to write the output to
outputFile = open('RST_TEST_EDU_Line_By_Line_Lowercase.txt', 'a')

print('# of Tokens that should be in EDU Hash: ', len(word_tokenize(fileToParse)))

## iterates through each file in the same directory as this program
for fn in os.listdir('.'):
    ## checks to see if a file has the below extension
    if fnmatch.fnmatch(fn, '*.out.edus'):
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
                if w == 0:
                    edu_hash[count] = '1'
                    count += 1
                elif w == len(tokens)-1:
                    edu_hash[count] = '2'
                    count += 1
                else:
                    edu_hash[count] = '3'
                    count += 1
            text = ' '.join([line])
        edu_hash[count] = '\n'
        count += 1
        outputFile.write(text)

print('EDU Hash length: ', len(edu_hash))

##with open('RST__TEST_EDU_Hash_Tags.dat', 'a') as finalFile:
##    print('Length of tags list: ', len(edu_hash.values()))
##    for v in range(0, len(edu_hash.values())):
##        finalFile.write(str(edu_hash.get(v)))
##        finalFile.write(' ')
##    print('EDU_hash values written to file.')

        
##with open('RST_EDU_Hash_1.dat', 'a') as finalFile:
##    finalFile.write(str(edu_hash))
##    print('EDU_hash written to file.')

