import nltk
import string
from nltk.corpus import stopwords

#Turns every filename on the command line into a document to be used in LDA.
def filesToDocuments(files):
    documents = []
    for file in files:
        documents.append(oneFileToDocument(file))
    return documents

#Cleans the documents of any unnecessary words, punctuation, or numbers.
def oneFileToDocument(file):
    #Turns file into one string.
    text = open(file).read()
    #Gets rid of numbers.
    text = nltk.re.sub(r'\d+', '', text)
    #Gets rid of punctuation and turns things into lowercase.
    text = "".join([char.lower() for char in text if char not in string.punctuation])
    words = nltk.word_tokenize(text)
    words = [w.lower() for w in words]
    stop_words = set(stopwords.words('english'))

    filtered_sentence = [w for w in words if not w in stop_words]

    filtered_sentence = []

    #Gets rid of stop words like "The" or "are".
    for w in words:
        if w not in stop_words and w not in "“":
            filtered_sentence.append(w)
    return filtered_sentence
