import json

import nltk
from nltk.corpus import stopwords

from FileToDocument import filesToDocuments, separateIntoDirtyWords, oneFileToDocument
from Tfidf import filterLowWordCount


def create_files(tweets, prefix, folderSuffix):
    outFolder = "resultingJSON" + folderSuffix
    in_files = ["relationship_bins/assoc_words.txt",
                "relationship_bins/child_words.txt",
                "relationship_bins/friend_words.txt",
                "relationship_bins/parent_words.txt",
                "relationship_bins/relative_words.txt",
                "relationship_bins/sib_words.txt",
                "relationship_bins/sig_other_words.txt",
                "relationship_bins/sub_words.txt",
                "relationship_bins/sup_words.txt"]

    out_files = [outFolder + "/assoc_words" + prefix + ".json",
                outFolder + "/child_words" + prefix + ".json",
                outFolder + "/friend_words" + prefix + ".json",
                outFolder + "/parent_words" + prefix + ".json",
                outFolder + "/relative_words" + prefix + ".json",
                outFolder + "/sib_words" + prefix + ".json",
                outFolder + "/sig_other_words" + prefix + ".json",
                outFolder + "/sub_words" + prefix + ".json",
                outFolder + "/sup_words" + prefix + ".json"]
    theTweets = []
    print("Turning the tweets into simple words...")
    for i in tweets:
        theTweets.append(separateIntoDirtyWords(i))
    theTweets = filterLowWordCount(theTweets, 5)
    for i in range(0, len(in_files)):
        open_one_file(in_files[i], out_files[i], theTweets, folderSuffix)

def open_one_file(inFilename, outFilename, tweets, extension):
    print("Reading from " + inFilename + " to " + outFilename + ".")
    a_file = open(inFilename, "r")
    list_of_lists = []
    for line in a_file:
        list_of_lists.append(line.lower()[:-1].split(" "))
    a_file.close()
    keptTweets = {}
    if (extension == "Same"):
        multTweetList = []
        multTweetList = tweetCheckLoop(multTweetList, tweets, list_of_lists)
        keptTweets['tweets'] = [j for i in multTweetList for j in i]
    else:
        keptTweets['tweets'] = []
        keptTweets['tweets'] = tweetCheckLoop(keptTweets['tweets'], tweets, list_of_lists)
    with open(outFilename, 'w') as outfile:
        json.dump(keptTweets, outfile)

def tweetCheckLoop(theList, tweets, list_of_lists):
    for i in tweets:
        for j in list_of_lists:
            if checkIfInList(j, i):
                theList.append(i)
    theList = cleanTweets(theList)
    return theList

def checkIfInList(A, B):
    for i in range(len(B)-len(A)+1):
        for j in range(len(A)):
            if B[i + j] != A[j]:
                break
        else:
            return True
    return False

def cleanTweets(tweets):
    stop_words = set(stopwords.words('english'))
    stemmer = nltk.stem.SnowballStemmer('english')

    theTweets = []

    for tweet in tweets:
        theTweets.append(oneFileToDocument(tweet, stop_words, stemmer))
    return theTweets