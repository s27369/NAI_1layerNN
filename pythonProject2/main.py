import os

from Util import *
from Perceptron import Perceptron
import string
languages = ["angielski", "francuski", "hiszpański", "niemiecki", "polski"]
test_folder = "data/test"
train_folder = "data/train"
test_file = "testfile"
train_file = "traintext"
label_name = "label"
alphabet = set(string.ascii_lowercase)
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
                yield txt_to_vector(f"{path}/{language}/{file}"), language

def get_dataset(type):
    if type=="test":
        path = test_folder
        file = test_file
    elif type == "train":
        path = train_folder
        file = train_file
    else:
        print("no such type")
        return
    dataset = {x:[] for x in alphabet}
    dataset[label_name] = []
    for d, lang in yield_data(path):
        for k, v in d.items():
            dataset[k].append(v)
            dataset[label_name].append(lang)
    return dataset

if __name__ == '__main__':

    # for data, _ in yield_data(train_folder, True):
    #     print(data)
    #     print(len(data))
    #     print(sum(data.values()))
    #     print("\n")
    train = get_dataset("train")
    dataset_info(train)

