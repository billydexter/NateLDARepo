class FormattedTweet:
    def __init__(self, country):
        self.wordList = []
        self.country = country

    def append(self, docWord):
        self.wordList.append(docWord)