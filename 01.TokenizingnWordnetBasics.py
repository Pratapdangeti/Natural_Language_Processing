__author__ = 'pratap'



# Tokenizing text into sentences


para = "Hello world. It's good to see you. Thanks for buying this book."

"""
from nltk.tokenize import sent_tokenize
print sent_tokenize(para)

import nltk.data
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
print tokenizer.tokenize(para)

"""


# Tokenizing sentences into words
from nltk.tokenize import word_tokenize
print word_tokenize('Hello World.')
print word_tokenize("can't")

from nltk.tokenize import TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()
print tokenizer.tokenize('Hello World. ')

























