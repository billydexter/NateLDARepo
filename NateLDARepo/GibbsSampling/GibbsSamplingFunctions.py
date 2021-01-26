from random import randint, random
from DocumentWord import DocumentWord
from FormattedTweet import FormattedTweet
import numpy as np

#Assigns each word in a tweet to a random group to prepare for the Gibbs sampling.
def getRandomGroups(numberOfGroups):
    groupNumber = randint(1, numberOfGroups)
    return "Group " + str(groupNumber)

#Assigns all the data into classes to prepare for the gibbs sampling.
def organizeData(tweetList):
    formattedTweetList = []
    wordDictionary = {}
    for tweet in tweetList:
        formattedTweetList.append(FormattedTweet(tweet['country']))
        for word in tweet['words']:
            docWord = DocumentWord(word, getRandomGroups(6))
            if word not in wordDictionary:
                docWord.id = 0
                wordDictionary[word] = []
                wordDictionary[word].append(docWord)
            else:
                docWord.id = len(wordDictionary[word])
                wordDictionary[word].append(docWord)
            formattedTweetList[len(formattedTweetList) - 1].append(docWord)
    return formattedTweetList, wordDictionary

#The function you run from main to do all the gibbs sampling.
#Iterations is how many times you want to run the algorithm,
#Tweetlist is a formatted list of all the tweets
#Word dictionary is the occurence and groups of each word.
#Word Dictionary and TweetList are made from the organizeData function.
def gibbsSampling(iterations, tweetList, wordDictionary):
    for i in range(0, iterations):
        gibbsSamplingIteration(tweetList, wordDictionary)

#One iteration of the gibbs sampling. See above for tweetList and wordDictionary.

def gibbsSamplingIteration(tweetList, wordDictionary):
    for tweet in tweetList:
        for word in tweet:
            oneGibbsSampling(word, wordDictionary[word.word], tweet, 0.5, 0.5)
    return tweetList, wordDictionary

#Runs gibbs sampling on one word. Gibbs sampling will assign words to topics
#similar to their document's topics and the other instances of the word's topics.
#word- The current instance of the word you are testing.
#wordInstances- All the instances of that word you are testing.
#tweet- The tweet you are testing.
#wordBias- A bias for occurence of a word. You're going to multiply them later
#    so you need a bias to avoid multiplying by 0.
#tweetBias- Same as word bias, but for occurence of a word in a tweet.
def oneGibbsSampling(word, wordInstances, tweet, wordBias, tweetBias):
    sameWordCount = [wordBias, wordBias, wordBias, wordBias, wordBias, wordBias]
    sameTweetCount = [tweetBias, tweetBias, tweetBias, tweetBias, tweetBias, tweetBias]
    for i in wordInstances:
        incrementGroupCount(i, sameWordCount)
    for i in tweet:
        incrementGroupCount(i, sameTweetCount)
    totalWordWeight = np.multiply(sameWordCount, sameTweetCount)
    totalWordWeight = totalWordWeight / sum(totalWordWeight)
    assignWord(word, totalWordWeight)
    return

#Gets the index of an array based on the group name.
def incrementGroupCount(foundGroup, groups):
    groupNumber = int(foundGroup[-1]) - 1
    groups[groupNumber] = groups[groupNumber] + 1
    return

#Assigns a word a group based on the tweet and other instances of this word.
#word- The instance of the word you wish to change.
#totalWordWeight- An array of weights that represent the likelihood you will
#change to that weight.
def assignWord(word, totalWordWeight):
    randomVal = random()
    bottomVal = 0
    for i in range(0, 6):
        bottomVal = bottomVal + totalWordWeight[i]
        if (randomVal < bottomVal):
            word.topic = "Group " + str(i + 1)
            return
    return "Group 6"
