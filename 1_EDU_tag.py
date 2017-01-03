import nltk, re, pprint, operator, sys, os, fnmatch, fileinput
from nltk import word_tokenize
from timeit import default_timer as timer

## fileToParse = open('RST_EDUs.txt').read()

## change dir to whereever dict is
hashdir = 'C:/Users/student/Dropbox/2016_05_RST/pRST/hash/'
#outdir = 'C:/Users/student/Dropbox/2016_05_RST/pRST/train/'
outdir = 'C:/Users/student/Documents/UVA/REU 16/MUST-CNN/RST/data/RSTtrees-WSJ-main-1.0/'

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

count = 0
os.chdir('C:/Users/student/Documents/UVA/REU 16/MUST-CNN/RST/data/RSTtrees-WSJ-main-1.0/')
finalFile = open('rst.tag.dat', 'w')
## change dir to whereever EDU Files are
#os.chdir('C:/Users/student/Documents/UVA/REU 16/MUST-CNN/RST/data/RSTtrees-WSJ-main-1.0/TEST')

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
        if w == 0:
            edu_hash[count] = '1'
        elif w == len(tokens)-1:
            edu_hash[count] = '2'
        else:
            edu_hash[count] = '3'
        finalFile.write(str(edu_hash[count])+' ')
        if dict.get(tokens[w]) == 'None':
            print('None came up, corresponding token: ', dict.get(tokens[w]))
        count += 1
    print(count)
    edu_hash[count] = '\n'
    finalFile.write('\n')
    count += 1

print('EDU Hash length: ', len(edu_hash), '; line: ',len(lines))


# with open(outdir+'rst.tag.dat', 'w') as finalFile:
#     print('Length of tags list: ', len(edu_hash.values()))
#     for v in range(0, len(edu_hash.values())):
#         finalFile.write(str(edu_hash.get(v)))
#         finalFile.write(' ')
#     print('EDU_hash values written to file.')


