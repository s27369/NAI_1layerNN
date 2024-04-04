import os

from Util import *
from Perceptron import Perceptron
import string
languages = ["angielski", "francuski", "hiszpański", "niemiecki", "polski"]
test_folder = "data/test"
train_folder = "data/train"
test_file = "testfile"
train_file = "traintext"
def txt_to_vector(filepath):
    with open(filepath, 'r',encoding="utf-8") as f:
        corpus = f.read()
    alphabet = set(string.ascii_lowercase)
    corpus = ''.join(char for char in corpus if char in alphabet)
    corups = corpus.lower()
    size = len(corpus)
    vec = {x:corpus.count(x)/size for x in alphabet}
    return vec

def yield_data(path, prnt=False):
    for language in os.listdir(path):
            for file in os.listdir(f"{path}/{language}"):
                if prnt: print(f"{path}/{language}/{file}")
                yield txt_to_vector(f"{path}/{language}/{file}")

if __name__ == '__main__':

    for data in yield_data(train_folder, True):
        print(data)
        print(len(data))
        print(sum(data.values()))
        print("\n")