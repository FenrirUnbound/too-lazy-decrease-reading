from __future__ import absolute_import, unicode_literals

from sumy.nlp.stemmers import Stemmer
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lsa import LsaSummarizer
from sumy.utils import get_stop_words


class Cliff:
    def __init__(self, language='english'):
        self.language = language
        self.summarizer = LsaSummarizer(Stemmer(language))
        self.summarizer.stop_words = get_stop_words(language)
    
    def process(self, document, sentences=8):
        parser = PlaintextParser.from_string(document, Tokenizer(self.language))

        result = []
        for sentence in self.summarizer(parser.document, sentences):
            result.append(str(sentence))

        return result