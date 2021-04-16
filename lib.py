from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize, sent_tokenize
from urllib.request import urlopen
from gensim.models import Word2Vec
import numpy as np
import string
import re
with open(r"texts\text.txt", "r") as f:
    sentences = [sentence.split() for sentence in f.readlines()]
model = Word2Vec(sentences, # главный аргумент - массив с предложениями, предложение - массив со словами
                 size=50, # размерность (количество координат в векторе), которая нам нужна
                 window=5, # на каком расстоянии слова будут считаться похожими
                 min_count=1, # будем добавлять слова, которые встретились хотя бы min_count раз
                 workers=4) # запустим параллельно в 4 процесса



def get_dist(text):
    #in comstruction
    length = len(text)
    fdist = FreqDist(word_tokenize(text))
    for el in fdist:
        fdist[el] /= length
    return fdist

def get_importance():
    common_in_language = urlopen('https://raw.githubusercontent.com/first20hours/google-10000-english/master/20k.txt')
    tokenized = word_tokenize(common_in_language.read().decode('utf-8'))
    return {el: i for i, el in enumerate(tokenized)}

def get_relevant(txtfreq, globrank, meaningfulness, k):
    def measure(x):
        try:
            return (meaningfulness[x]) * (txtfreq[x]) * (-abs(globrank[x]-int(k*len(globrank)))+(len(globrank)//2))
        except KeyError:
            return float('-inf')
    ans = []
    for i in sorted(txtfreq.keys(), key=measure, reverse=True)[:10]:
        ans.append(i)
        #print(i)
    return ans


def get_meaningfulness(txt):
    result = dict()
    result_counts = dict()
    
    text = txt
    sentences = sent_tokenize(text)

    average = np.zeros(50)
    firstword = True
    for sent in sentences:
        # clean sentence
        Sentence = word_tokenize(sent)
        Sentence = [w.lower() for w in Sentence if re.findall('\W+',w) != [w]]
        
        for wordi in range(len(Sentence)):
            sum_vectors = np.zeros(50)
            word = Sentence[wordi]
            
            divisor = wordi
            if divisor == 0:
                if Sentence[0] not in model.wv or firstword:              
                    continue

                coef = np.corrcoef(model.wv[word], average)[0][1]
                dissim = 1-coef
                
                result[word] = result.get(word, 0) + dissim
                result_counts[word] = result_counts.get(word, 0) + 1
                continue
                
            else:
                for i in range(wordi):               
                    iter_word = Sentence[i]

                    if iter_word not in model.wv:
                        continue
                    
                    else:
                        sum_vectors += model.wv[iter_word]
                
                average = sum_vectors/divisor
                
                # calculate correlation
                if word not in model.wv:
                    continue
                
                coef = np.corrcoef(model.wv[word.lower()], average)[0][1]
                dissim = 1-coef
                
                result[word] = result.get(word, 0) + dissim
                result_counts[word] = result_counts.get(word, 0) + 1
        firstword = False

    for key in result:
        result[key] /= result_counts[key]
    return result