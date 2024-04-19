import os

from matplotlib import pyplot as plt

from Util import *
from Layer import Layer
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
    return string_to_vector(corpus)

def string_to_vector(s, Label=False):
    alphabet = set(string.ascii_lowercase)
    s = s.lower()
    s = ''.join(char for char in s if char in alphabet)
    size = len(s)
    vec = {x: s.count(x) / size for x in alphabet}
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

def vec_to_dataset(vec):
    dataset = {x: [] for x in alphabet}
    dataset[label_name] = []
    for k, v in vec.items():
        dataset[k].append(v)
    return dataset
def test_model(dataset, model, prnt=False):
    predictions = []
    for i in range(len(dataset[label_name])):
        obs = get_observation(dataset, i)
        p = model.predict(obs)
        predictions.append(p)
        if prnt: print(f"Classified {obs[-1]} as {p} ")

    acc = 0
    for x in range(len(predictions)):
        if dataset[label_name][x]==predictions[x]:
            acc+=1
    if prnt:print(f"Accuracy={acc/len(predictions)}")
    return acc/len(predictions)

def get_plot(dic):
    max_acc, min_acc = max(dic.values()), min(dic.values())
    plt.plot( dic.keys(),dic.values() )
    plt.xlabel("Num of iterations")
    plt.ylabel("Accuracy")
    plt.title("Accuracy vs num of iterations")
    plt.axhline(y=max_acc, color='green')
    plt.text(x=0, y=max_acc, s=f'Max accuracy: {max_acc}', color='green', fontsize=8, verticalalignment='bottom')
    plt.axhline(y=min_acc, color='red')
    plt.text(x=0, y=min_acc, s=f'Min accuracy: {min_acc}', color='red', fontsize=8, verticalalignment='bottom')
    plt.show()
def interface(test,train, languages):
    model = Layer(get_num_of_attributes(train), languages, 0.5, 10)
    quit=False
    while not quit:
        print("Choose number:\n1 - input sample text to classify\n2 - test model\n3 - get accuracy graph per learning rate for given bias\n4 - quit\n>>>", end="")
        try:
            i = int(input())
        except:
            print("Incorrect input.")
            continue
        if i == 1:
            try:
                txt = input("input text\n>>>")
                vec = string_to_vector(txt)
                d = vec_to_dataset(vec)
                d[label_name]="unknown"
                obs = get_observation(d, 0)
                print(model.predict(obs))
            except:
                print("incorrect input")
        elif i == 2:
                print(test_model(test, model, True))
        elif i==3:
            try:
                b = int(input("bias (int)\n>>>"))
                acc = {}
                for i in range(1, 100):
                    layer = Layer(get_num_of_attributes(train), languages, i/100, b)
                    layer.train_layer(train, 100)
                    result =  test_model(test, layer)
                    acc[i / 100] =result
                    if result == 1:
                        model = layer
                        break
                print(acc)
                key = next((k for k, v in acc.items() if v == max(acc.values())), None)
                print(max(acc.values()), key)
                get_plot(acc)
            except:
                print("incorrect input")
        elif i == 4:
            return
        else:
            print("Incorrect input.")
if __name__ == '__main__':

    # for data, _ in yield_data(train_folder, True):
    #     print(data)
    #     print(len(data))
    #     print(sum(data.values()))
    #     print("\n")
    train = get_dataset("train")
    dataset_info(train)
    layer = Layer(get_num_of_attributes(train), languages, 0.5, 10)
    layer.train_layer(train, 100)

    test = get_dataset("test")
    dataset_info(test)
    test_model(test, layer, True)
    interface(test,train, languages)
