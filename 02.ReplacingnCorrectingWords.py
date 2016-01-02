__author__ = 'pratap'

# Porter Stemmer
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
print stemmer.stem('cooking')
print stemmer.stem('cookery')

# Lancaster Stermmer
from nltk.stem import LancasterStemmer
lanc_stemmer = LancasterStemmer()
print lanc_stemmer.stem('cooking')
print lanc_stemmer.stem('cookery')




