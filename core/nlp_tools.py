"""memgpt/core/nlp_tools.py

import nltk
from nltk.tokenize import word_tokenize

class NLPTools:
    def __init__(self):
        # Download NLTK data if not already present
        nltk.download('punkt', quiet=True)

    def process_text(self, text):
        # Tokenize text
        tokens = word_tokenize(text)
        # Convert to lowercase
        tokens = [token.lower() for token in tokens]
        # Rejoin tokens
        processed_text = ' '.join(tokens)
        return processed_text
"""