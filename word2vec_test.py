
with open(r"texts\text.txt", "r") as f:
    sentences = [sentence.split() for sentence in f.readlines()]

model = Word2Vec(sentences, # главный аргумент - массив с предложениями, предложение - массив со словами
                 size=200, # размерность (количество координат в векторе), которая нам нужна
                 window=5, # на каком расстоянии слова будут считаться похожими
                 min_count=1, # будем добавлять слова, которые встретились хотя бы min_count раз
                 workers=4) # запустим параллельно в 4 процесса

print(model.wv['the'])

