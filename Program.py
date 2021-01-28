import tkinter as tk
from tkinter import filedialog
from lib import get_dist, get_importance, get_relevant

class Program(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.difficulty = 1/2
        self.word_ranks = get_importance()
        #'print' analogy
        self.top_line = tk.Label(self, text='')
        self.top_line.pack()

        self.txt_select_button = tk.Button(self, text='Select your text', command=self.get_given_text)
        self.txt_select_button.pack()

        self.bottom_text = tk.Label(self, text='')
        self.bottom_text.pack()

    def write(self, ln, txt):
        ln['text'] = txt

    def get_given_text(self):
        initial_txt_path = r'C:\\Users\\egors\\OneDrive\Documents\\GitHub\\LanguageLearningHepler\\texts\\text.txt'
        self.given_text_filename = filedialog.askopenfilename(initialdir=initial_txt_path)
        
        self.write(self.top_line, 'File loaded')
        self.start_functional_part()

    def start_functional_part(self):
        self.analize_button = tk.Button(self, text='Get the most relevant words', command=self.get_relevant_words)
        self.analize_button.pack()

        self.up_diff = tk.Button(self, text='Harder', command=lambda: self.dif(1))
        self.down_diff = tk.Button(self, text='Easier', command=lambda: self.dif(-1))
        self.up_diff.pack()
        self.down_diff.pack()
    def get_relevant_words(self):
        #in construction
        text = open(self.given_text_filename, 'r', encoding='utf-8').read()
        self.distribution = get_dist(text)
        self.write(self.bottom_text, '\n'.join(get_relevant(self.distribution, self.word_ranks, self.difficulty)))

    def dif(self, x):
        self.difficulty += x*(1/8)
        self.write(self.top_line, f'Difficlty: {self.difficulty}')
        self.write(self.bottom_text, '\n'.join(get_relevant(self.distribution, self.word_ranks, self.difficulty)))
