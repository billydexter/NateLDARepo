#Class for a word. Each word has a name, a topic, and an id.

class DocumentWord:
    word = ""
    topic = ""
    id = -1
    def __init__(self, word, topic):
        self.word = word
        self.topic = topic

    def setID(self, id):
        self.id = id