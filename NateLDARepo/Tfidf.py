from gensim import corpora
from gensim import models

#Drops words that don't appear more than the minimum amount
#of times in all the documents.
def filterLowWordCount(tweets, minimum):
    from collections import defaultdict
    frequency = defaultdict(int)
    for tweet in tweets:
        for token in tweet:
            frequency[token] += 1
    return [[token for token in text if frequency[token] >= minimum] for text in tweets]

#Determines how important words are based on how much they appear in a
#document and how much they appear in every document. Every word in a
#document is given a score between 0 and 1. After the TFIDF is done,
#every word that has a score below the minimum cutoff will be dropped.
#Might be made more efficient later on.
def tfidf(documents, minimumCutoff):
    dictionary = corpora.Dictionary(documents)
    bow_corpus = [dictionary.doc2bow(text) for text in documents]
    tfidf = models.TfidfModel(bow_corpus)
    for i in documents:
        tfMeasure = tfidf[dictionary.doc2bow(i)]
        valsToRemove = []
        dict_1 = dict()
        for id, score in tfMeasure:
            dict_1.setdefault(id, []).append(score)
        for j in range(0, len(i)):
            wordID = dictionary.token2id[i[j]]
            freq = dict_1[wordID][0]
            if freq < minimumCutoff:
                valsToRemove.append(j)
        for x in reversed(valsToRemove):
            del i[x]
    return documents


