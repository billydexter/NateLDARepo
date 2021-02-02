#The main function of the LDA preparation so far. To run this file so far, run
#"python LDAMain.py [filenames]. It will read all the files and convert them into documents
#and words, so the gibbs sort and LDA can be ran on them.

#if the import statements don't work, try from NateLDARepo.FileToDocument import filesToDocuments
#for each level.
from FileToDocument import filesToDocuments, extractJSON
from Tfidf import tfidf, filterLowWordCount

import sys
import json

files = []
#Get the file arguments from the command line.
for i in range(1, 3):
    files.append(sys.argv[i])
if len(files) < 2:
    print("Include the indian and american JSON files in the command line arguments.")
    exit()

#Get the minimum frequency and tfidf threshold from the command line.
#
#Minimum frequency is the minimum amount of times a word must appear in
#the documents in order to count for the analysis. It is the third command
#line argument behind the json files.
#
#TfidfThreshold is the minimum TFIDF a word must have in a document in order
#to be counted as relevant. It is the fourth command line argument behind the
#json files. If you do not specify this number, no TFIDF will be ran.
#
minimumFrequency = 5
if len(sys.argv) > 3:
    minimumFrequency = int(sys.argv[3])
tfidfThreshold = -1
if len(sys.argv) > 4:
    tfidfThreshold = float(sys.argv[4])

#extract JSON turns the files into a list of strings of text.
print("Extracting the indian tweets from the JSON file...\n")
indianTweets = extractJSON(files[0])


#format and clean the words from the JSON file.
print("Cleaning the strings inside the indian tweets...\n")
indianDocuments = filesToDocuments(indianTweets)

#Removes words that do not appear frequently in the document.
print("Removing words that don't appear often in the indian documents...\n")
indianDocuments = filterLowWordCount(indianDocuments, minimumFrequency)

#TFIDF assigns each word a value between 0 and 1 depending on how important
#the algorithm decides each word is. This is a very computationally
#intensive algorithm, with both the american and indian tweets taking about
#3 minutes to run on the lab machines. It will drop values that are below
#the threshold of being measured as important.
if (tfidfThreshold != -1):
    print("Running TFIDF on the indian documents...\n")
    indianDocuments = tfidf(indianDocuments, tfidfThreshold)

#Does the same process for the American tweets as the Indian tweets.
print("Extracting the american tweets from the JSON file...\n")
americanTweets = extractJSON(files[1])
print("Cleaning the strings inside the american tweets...\n")
americanDocuments = filesToDocuments(americanTweets)
print("Removing words that don't appear often in the american documents...\n")
americanDocuments = filterLowWordCount(americanDocuments, minimumFrequency)
if (tfidfThreshold != -1):
    print("Running TFIDF on the indian documents...\n")
    americanDocuments = tfidf(americanDocuments, tfidfThreshold)
#Exports the data into a new JSON file named tweetDocuments.json
#NOTE: Running emoji does not work properly if running on Linux.
print("Converting indian and american tweets into a JSON file...\n")
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

with open('tweetDocuments.json', 'w') as outfile:
    json.dump(tweets, outfile)

print("Done")
