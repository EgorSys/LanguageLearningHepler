import pandas as pd

df = pd.read_csv('vectors\glove.6B.50d.txt', sep=" ", quoting=3, header=None, index_col=0)
glove = {key: val.values for key, val in df.T.items()}