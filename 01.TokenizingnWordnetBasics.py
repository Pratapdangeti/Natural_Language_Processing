__author__ = 'pratap'



# Tokenizing text into sentences


para = "Hello world. It's good to see you. Thanks for buying this book."

"""
from nltk.tokenize import sent_tokenize
print sent_tokenize(para)

import nltk.data
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
print tokenizer.tokenize(para)




# Tokenizing sentences into words
from nltk.tokenize import word_tokenize
print word_tokenize('Hello World.')
print word_tokenize("can't")

from nltk.tokenize import TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()
print tokenizer.tokenize('Hello World. ')


# Word punct tokenizer
from nltk.tokenize import WordPunctTokenizer
tokenizer = WordPunctTokenizer()
print tokenizer.tokenize("Can't is a contraction.")

# Tokenizing sentences using Regex
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer("[\w']+")
print tokenizer.tokenize("Can't is a contraction.")


from nltk.tokenize import regexp_tokenize
print regexp_tokenize("Can't is a contraction.","[\w']+")

swtokenizer = RegexpTokenizer('\s+', gaps=True)
print swtokenizer.tokenize("Can't is a contraction.")

"""


# filtering stopwords in a tokenized sentence
from nltk.corpus import stopwords
english_stops = set(stopwords.words('english'))
words = ["Can't",'is','a','contraction']
print [word for word in words if word not in english_stops]



# looking up synsets for a word in wordnet
from nltk.corpus import wordnet
syn = wordnet.synsets('cookbook')[0]
print syn.name
print syn.definition

print wordnet.synsets('cooking')[0].examples
































