from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from urllib.request import urlopen

def get_dist(text):
    #in comstruction

    fdist = FreqDist()
    for word in word_tokenize(text):
        fdist[word.lower()] += 1
    return fdist

def get_importance():
    common_in_language = urlopen('https://raw.githubusercontent.com/first20hours/google-10000-english/master/20k.txt')
    tokenized = word_tokenize(common_in_language.read().decode('utf-8'))
    return {el: i for i, el in enumerate(tokenized)}

def get_relevant(txtfreq, globrank, k):
    def measure(x):
        try:
            return txtfreq[x]*(-abs(globrank[x]-int(k*len(globrank)))+(len(globrank)//2))
        except KeyError:
            return float('-inf')
    ans = []
    for i in sorted(txtfreq.keys(), key=measure, reverse=True)[:10]:
        ans.append(i)
    return ans

'''

def get_hlexis_rating(globrank, words):
    return 
'''

#def needed_words(text)