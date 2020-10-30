import tkinter as tk
from tkinter import filedialog
from lib import get_dist, get_importance, get_relevant

class Program(tk.Frame):
    def __init__(self, master):
        super().__init__()
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
        self.given_text_filename = filedialog.askopenfilename(initialdir=r'C:\Users\egors\OneDrive\Documents\GitHub\LanguageLearningHepler\texts\text.txt')
        
        self.write(self.top_line, 'File loaded')
        self.start_functional_part()

    def start_functional_part(self):
        self.analize_button = tk.Button(self, text='Get the most relevant words', command=self.get_relevant_words)
        self.analize_button.pack()

    def get_relevant_words(self):
        #in construction
        text = open(self.given_text_filename, 'r', encoding='utf-8').read()
        distribution = get_dist(text)
        self.write(self.bottom_text, '\n'.join(get_relevant(distribution, self.word_ranks)))