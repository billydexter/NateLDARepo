import json
import nltk
import string
from emoji.unicode_codes import UNICODE_EMOJI
from nltk.corpus import stopwords
from emoji import demojize

#Turns every filename on the command line into a document to be used in LDA.
def filesToDocuments(tweets):
    documents = []
    #sets the stopwords once so you don't have to do it every iteration. For performance.
    stop_words = set(stopwords.words('english'))
    stemmer = nltk.stem.SnowballStemmer('english')
    for tweet in tweets:
        newWords = separateIntoDirtyWords(tweet)
        documents.append(oneFileToDocument(newWords, stop_words, stemmer))
    return documents

#Cleans the documents of any unnecessary words, punctuation, or numbers.
def oneFileToDocument(newWords, stop_words, stemmer):
    #Gets rid of punctuation marks.
    table = str.maketrans('', '', string.punctuation)
    words = [w.translate(table) for w in newWords]
    #Gets rid of stop words and words that are less than 3 letters long.
    words = [stemmer.stem(w) for w in words if not w in stop_words and len(w) > 2]

    return words

def separateIntoDirtyWords(tweet):
    # Gets rid of numbers.
    text = nltk.re.sub(r'\d+', '', tweet)
    # Gets rid of punctuation and turns things into lowercase.
    text = demojize(text).replace(':', ' ')
    words = text.split()
    # The loop changing special characters.
    newWords = []
    for i in range(0, len(words)):
        if (words[i][0] == "@"):
            pass
        elif (words[i][0] == "#"):
            newWords.append(words[i][1:].lower())
        elif (len(words[i]) > 3 and (words[i][0:4] == "http" or words[i][0:2] == "//")):
            pass
        elif (len(words[i]) > 14 and words[i][0:15] == "pic.twitter.com"):
            pass
        else:
            newWords.append(deSpecialCharacter(words[i].lower()))
    return newWords

#Turns a JSON file into a list of tweets.
def extractJSON(file):
    with open(file) as file:
        data = json.load(file)
        tweetList = list(data)
        validTweets = []
        for i in range(0, len(tweetList)):
            if data[tweetList[i]][0] == "VALID":
                validTweets.append(tweetList[i])
        return validTweets

#Detects unusual ascii characters and will save them as emojis if needed.
def deSpecialCharacter(inputString):
    return inputString.encode('ascii', 'ignore').decode('ascii')

#Detects if a character is an emoji, and if so, it adds it to the end of the list.
def testEmojiCharacter(emojiCharacter, words):
    try:
        emojiTest = UNICODE_EMOJI[emojiCharacter]
        words.append(emojiTest + "emoji")
    except KeyError:
        pass
