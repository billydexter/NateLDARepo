import sys

from FileToDocument import extractJSON, filesToDocuments
from FileCreationHelper import create_files

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

#extract JSON turns the files into a list of strings of text.
print("Extracting the indian tweets from the JSON file...\n")
indianTweets = extractJSON(files[0])

print("Cleaning the strings inside the indian tweets...\n")
indianDocuments = filesToDocuments(indianTweets)
create_files(indianDocuments, "_india")

print("Extracting the american tweets from the JSON file...\n")
americanTweets = extractJSON(files[1])

print("Cleaning the strings inside the american tweets...\n")
americanDocuments = filesToDocuments(americanTweets)
create_files(americanDocuments, "_america")

