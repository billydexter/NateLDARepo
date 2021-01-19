import scipy
import numpy as np
import math

#Documents are a list of a list of DocumentWords, and DocumentWords are a tuple of word and topic.
class PoissonSampling:

    #Function takes in a list of documents, and randomly returns a sample of poisson distributed numbers
    #for the number of words sampled per document.
    def getPoissonSampleNumber(self, documents):
        wordCount = 0
        k = 0
        documentCount = len(documents)
        for document in documents:
            wordCount += len(document)
        if (documentCount > 0):
            #K is the expected value in the Poisson distribution. It's the average number of words in
            #a document.
            k = wordCount / documentCount
        wordNumbers = []
        for document in documents:
            #Gets a random number of words from the poisson distribution, rounded to the nearest whole number.
            wordNumbers.append((np.random.poisson(k, len(documents)))[0])

        return wordNumbers
