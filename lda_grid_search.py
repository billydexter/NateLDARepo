import json

# Text processing libraries
import re, nltk, spacy, gensim

# LDA Model and grid search libraries
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation, TruncatedSVD
from sklearn.model_selection import GridSearchCV

# spacy 'en' model
nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])


def load_data(file_path):
    """
    loads in tweet data from json file and returns a list of tweets where each tweet is
    a list of words

    params:
        file_path (str): path to tweet file
    """
    with open(file_path) as f:
        tweets = json.load(f)
    return tweets["tweets"]


def lemmatization(texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
    """
    Convert words into their root words.
    For example studying --> study, meeting --> meet, ect..
    """
    texts_out = []
    for sent in texts:
        doc = nlp(" ".join(sent))
        texts_out.append(" ".join([token.lemma_ if token.lemma_ not in ['-PRON-'] else '' for token in doc if token.pos_ in allowed_postags]))
    return texts_out

def run_lda(tweets):
    """
    Runs LDA on tweet data and returns the topic coherence score for the model
    :param tweets:
    :return: topic
    """
    # lemmatize words in tweet data
    data_lemmatized = lemmatization(tweets, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV'])

    # initialize count vectorizer
    vectorizer = CountVectorizer(analyzer='word',
                                 min_df=10,  # minimum reqd occurences of a word
                                 stop_words='english',  # remove stop words
                                 lowercase=True,  # convert all words to lowercase
                                 token_pattern='[a-zA-Z0-9]{3,}',  # num chars > 3
                                 # max_features=50000,             # max number of uniq words
                                 )

    data_vectorized = vectorizer.fit_transform(data_lemmatized)

    lda_model = LatentDirichletAllocation(n_components=20,  # Number of topics
                                          max_iter=10,  # Max learning iterations
                                          learning_method='online',
                                          random_state=100,  # Random state
                                          batch_size=128,  # n docs in each learning iter
                                          evaluate_every=-1,  # compute perplexity every n iters, default: Don't
                                          n_jobs=-1,  # Use all available CPUs
                                          )

    lda_model.fit_transform(data_vectorized)

    print("Log Likelihood: ", lda_model.score(data_vectorized))
    print("Perplexity: ", lda_model.perplexity(data_vectorized))


if __name__ == "__main__":
    tweets = load_data("/Users/natecarlson/Research/NateLDARepo/NateLDARepo/resultingJSON/friend_words_america.json")
    run_lda(tweets)
