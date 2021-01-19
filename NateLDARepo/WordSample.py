
#A list of lists of strings.
import random
class WordSample:

    #Gets a sample of words from one document.
    #n is the number of words you wish to get
    #document is the document you want to get words from.
    def getRandomWords(self, n, document):
        return random.choices(document, k=n)

    #Gets a sample of words from a list of documents.
    #Word count is the number of words you wish to get
    #documents is the list of documents.
    def getRandomWordsForEachDocument(self, wordCount, documents):
        randomWords = []
        for i in range(0, len(documents)):
            randomDoc = self.getRandomWords(wordCount[i], documents[i])
            randomWords.append(randomDoc)
        return randomWords
