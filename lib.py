from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize

def get_dist(text):
    #in comstruction

    fdist = FreqDist()
    for word in word_tokenize(text):
        fdist[word.lower()] += 1

    return fdist