#The main function of the LDA preparation so far. To run this file so far, run
#"python LDAMain.py [filenames]. It will read all the files and convert them into documents
#and words, so the gibbs sort and LDA can be ran on them.

#if the import statements don't work, try from NateLDARepo.FileToDocument import filesToDocuments
#for each level.
from FileToDocument import filesToDocuments, extractJSON

import sys
import json

files = []
#Get the file arguments from the command line.
for i in range(1, len(sys.argv)):
    files.append(sys.argv[i])
if len(files) < 2:
    print("Include the indian and american JSON files in the command line arguments.")
    exit()

#extract JSON turns the files into a list of strings of text.
indianTweets = extractJSON(files[0])


#format and clean the words from the JSON file.
indianDocuments = filesToDocuments(indianTweets)


americanTweets = extractJSON(files[1])
americanDocuments = filesToDocuments(americanTweets)

tweets = {}
tweets['tweets'] = []
for i in indianDocuments:
    tweets['tweets'].append({
        'country': 'India',
        'words': i
    })

for i in americanDocuments:
    tweets['tweets'].append({
        'country': 'USA',
        'words': i
    })

with open('tweetDocuments.txt', 'w') as outfile:
    json.dump(tweets, outfile)
