import nltk

class Article:
    def __init__(self, article_string):
        self.text = article_string
        
    def tokens(self):
        return nltk.word_tokenize(self.text)