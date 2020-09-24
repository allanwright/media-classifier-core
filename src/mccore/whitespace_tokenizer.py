'''Defines a tokenizer that only splits on spaces.

'''

from spacy.tokenizer import Tokenizer
from spacy.tokens import Doc

class WhitespaceTokenizer(Tokenizer):
    '''Defines a tokenizer that only splits on spaces.

    '''

    def __init__(self, vocab):
        super(WhitespaceTokenizer, self).__init__(vocab)

    def __call__(self, text):
        words = text.rstrip().split(' ')
        spaces = [True] * len(words)
        return Doc(self.vocab, words=words, spaces=spaces)
