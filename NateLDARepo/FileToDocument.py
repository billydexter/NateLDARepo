import json
import nltk
import string
from emoji.unicode_codes import UNICODE_EMOJI
from nltk.corpus import stopwords

#Turns every filename on the command line into a document to be used in LDA.
def filesToDocuments(tweets):
    documents = []
    #sets the stopwords once so you don't have to do it every iteration. For performance.
    stop_words = set(stopwords.words('english'))
    for tweet in tweets:
        documents.append(oneFileToDocument(tweet, stop_words))
    return documents

#Cleans the documents of any unnecessary words, punctuation, or numbers.
def oneFileToDocument(tweet, stop_words):
    #Gets rid of numbers.
    text = nltk.re.sub(r'\d+', '', tweet)
    #Gets rid of punctuation and turns things into lowercase.
    words = text.split()
    #The loop changing special characters.
    for i in range(0, len(words)):
        if (words[i][0] == "@"):
            words[i] = "[MENTION]"
        elif (words[i][0] == "#"):
            words[i] = "[HASHTAG]"
        elif (len(words[i]) > 1 and words[i][0:4] == "http"):
            words[i] = "[URL]"
        elif (len(words[i]) > 14 and words[i][0:15] == "pic.twitter.com"):
            words[i] = "[PICTURE]"
        else:
            words[i] = deEmojify(words[i].lower(), words)
    #Gets rid of punctuation marks.
    table = str.maketrans('', '', string.punctuation)
    words = [w.translate(table) for w in words]
    #Gets rid of stop words and words that are less than 3 letters long.
    words = [w for w in words if not w in stop_words and len(w) > 2]

    return words

#Turns a JSON file into a list of tweets.
def extractJSON(file):
    with open(file) as file:
        data = json.load(file)
        tweetList = list(data)
        return tweetList

#Detects unusual ascii characters and will save them as emojis if needed.
def deEmojify(inputString, words):
    if (inputString.encode('ascii', 'ignore').decode('ascii') != inputString):
        for letter in inputString:
            testEmojiCharacter(letter, words)
    return inputString.encode('ascii', 'ignore').decode('ascii')

#Detects if a character is an emoji, and if so, it adds it to the end of the list.
def testEmojiCharacter(emojiCharacter, words):
    try:
        emojiTest = UNICODE_EMOJI[emojiCharacter]
        words.append(emojiTest + "emoji")
    except KeyError:
        pass
