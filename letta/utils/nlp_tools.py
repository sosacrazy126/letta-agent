import nltk
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer

class NLPTools:
    def __init__(self):
        nltk.download('punkt', quiet=True)
        nltk.download('vader_lexicon', quiet=True)
        self.sia = SentimentIntensityAnalyzer()

    def process_text(self, text):
        tokens = word_tokenize(text.lower())
        sentiment = self.analyze_sentiment(text)
        return {
            'tokens': tokens,
            'sentiment': sentiment
        }

    def analyze_sentiment(self, text):
        sentiment_scores = self.sia.polarity_scores(text)
        if sentiment_scores['compound'] >= 0.05:
            return 'positive'
        elif sentiment_scores['compound'] <= -0.05:
            return 'negative'
        else:
            return 'neutral'