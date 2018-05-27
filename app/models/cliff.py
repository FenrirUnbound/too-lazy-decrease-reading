from __future__ import absolute_import, unicode_literals

from sumy.nlp.stemmers import Stemmer
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.kl import KLSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.utils import get_stop_words


class Cliff:
    def __init__(self, language='english'):
        stemmer = Stemmer(language)

        self.language = language
        self.algorithms = {
            'kl': KLSummarizer(stemmer),
            'lex_rank': LexRankSummarizer(stemmer),
            'lsa': LsaSummarizer(stemmer),
            'text_rank': TextRankSummarizer(stemmer)
        }
        for alg in self.algorithms:
            self.algorithms[alg].stop_words = get_stop_words(language)

    
    def process(self, document, sentences=8, algorithm='lsa'):
        summarizer = self.algorithms[algorithm]
        parser = PlaintextParser.from_string(document, Tokenizer(self.language))

        result = []
        for sentence in summarizer(parser.document, sentences):
            result.append(str(sentence))

        return result