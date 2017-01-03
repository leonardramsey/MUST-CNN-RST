import nltk, re, pprint, operator, sys, os, fnmatch, fileinput
from nltk import word_tokenize
from timeit import default_timer as timer

## fileToParse = open('RST_EDUs.txt').read()

outdir = 'C:/Users/student/Documents/UVA/REU 16/MUST-CNN/RST/data/RSTtrees-WSJ-main-1.0/'
#outdir = 'C:/Users/student/Dropbox/2016_05_RST/pRST/test/'

## change dir to whereever dict is
##os.chdir('C:/Users/student/Dropbox/2016_05_RST/pRST/hash')
#dict = set(open('word.lst').read().splitlines())
input_file = open('word_full.lst', 'r')

dict = {}
count_lines = 0
for line in input_file:
    word = line.strip()
    dict[word]= count_lines
    count_lines += 1
    ## print(word, " ", count_lines)
##print('number of lines:', count_lines)
##print('Length of dict: ', len(dict))

edu_hash = {}
##edu_hash['B'] = 1 ## beginning of EDU
##edu_hash['E'] = 2 ## ending of EDU
##edu_hash['N'] = 3 ## no break in EDU


## opens the file to write the output to
## outputFile = open('RST_EDU_Compilation_ALbyL.txt', 'a')


os.chdir('C:/Users/student/Documents/UVA/REU 16/MUST-CNN/RST/data/RSTtrees-WSJ-main-1.0/')
finalFile2 = open('word.dat', 'w')

## change dir to whereever EDU Files are
#os.chdir('C:/Users/student/Documents/UVA/REU 16/MUST-CNN/RST/data/RSTtrees-WSJ-main-1.0/TEST')
count = 0
## iterates through each file in the same directory as this program
tempFile = open('RST_ALL_EDUs.txt')
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
        if tokens[w]=='':
            continue
        finalFile2.write(str(dict.get(tokens[w])))
        finalFile2.write(" ")
        edu_hash[count] = str(dict.get(tokens[w]))
        if dict.get(tokens[w]) == None:
            print('None came up, corresponding token: ', dict.get(tokens[w]), ',count:', count, '\nPreceding token:', tokens[w-1], '\nLine: ', line)
        count += 1
    print(count)
    edu_hash[count] = '\n'
    finalFile2.write('\n')
    count += 1

print('EDU Hash length: ', len(edu_hash), '; line: ',len(lines))


# with open(outdir+'word.dat', 'w') as finalFile:
#     print('Length of tags list: ', len(edu_hash.values()))
#     for v in range(0, len(edu_hash.values())):
#         finalFile.write(str(edu_hash.get(v)))
#         finalFile.write(' ')
#     print('EDU_hash values written to file.')
