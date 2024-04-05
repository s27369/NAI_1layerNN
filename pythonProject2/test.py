import os
import re

from matplotlib import pyplot as plt

test_folder = "data/test"
train_folder = "data/train"
languages = ["angielski", "francuski", "hiszpański", "niemiecki", "polski"]
def mean(list):
    return sum(list)/len(list)
def language_stats(path, filename):
    print(path)
    for folder in os.listdir(path):
        print(f"{folder}: ", end="")
        l = []
        for i in range(1,11):
            with open(f"{path}/{folder}/{filename}_{i}.txt", 'r', encoding='utf-8') as f:
                text = f.read()
                l.append(len(text))
        print(f"avg={mean(l)}, max={max(l)}, min={min(l)}")
def create_files(path, filename):
    for folder in os.listdir(path):
        for i in range(1,11):
            with open(f"{path}/{folder}/{filename}_{i}.txt", 'w'):
                pass
# def rename_files(path, extension):
#     for folder in os.listdir(path):
#         for file in (f"{path}/{folder}"):
#             os.rename(f"{path}/{folder}/{file}", f"data/{folder}/traintext_10")
def clean_text(path, filename):
    pattern = r'\[.*?\d.*?\]'
    for folder in os.listdir(path):
        for i in range(1,11):
            print(f"{path}/{folder}/{filename}_{i}.txt")
            with open(f"{path}/{folder}/{filename}_{i}.txt", 'r+', encoding='utf-8') as f:
                text = f.read()
                text= re.sub(pattern, '', text)
                text = text.replace('\n', '')
                f.seek(0)
                f.write(text)
                f.truncate()
def get_text_lengths(path, language, filename):
    for i in range(1,11):
        print(f"{path}/{language}/{filename}_{i}.txt", end=" length: ")
        with open(f"{path}/{language}/{filename}_{i}.txt", 'r', encoding='utf-8') as f:
            text = f.read()
            print(len(text))
def create_folders(path, languages):
    for language in languages:
        os.mkdir(f"{path}/{language}")
    print(os.listdir(path))

def get_plot(dic):
    max_acc, min_acc = max(dic.values()), min(dic.values())
    plt.plot( dic.keys(), dic.values())
    plt.xlabel("Num of iterations")
    plt.ylabel("Accuracy")
    plt.title("Accuracy vs num of iterations")
    plt.axhline(y=max_acc, color='green')
    plt.text(x=0, y=max_acc, s=f'Max accuracy: {max_acc}', color='green', fontsize=8, verticalalignment='bottom')
    plt.axhline(y=min_acc, color='red')
    plt.text(x=0, y=min_acc, s=f'Min accuracy: {min_acc}', color='red', fontsize=8, verticalalignment='bottom')
    plt.show()
if __name__ == '__main__':
    # create_folders(test_folder, languages)
    # create_files(test_folder, "testfile")
    # clean_text(test_folder, "testfile")
    # get_text_lengths(test_folder, "angielski", "testfile")
    # get_text_lengths(test_folder, "polski", "testfile")
    # language_stats(test_folder, "testfile")
    get_plot({0.01: 0.8, 0.02: 0.66, 0.03: 0.66, 0.04: 0.8, 0.05: 0.82, 0.06: 0.82, 0.07: 0.6, 0.08: 0.68, 0.09: 0.64, 0.1: 0.6, 0.11: 0.6, 0.12: 0.5, 0.13: 0.56, 0.14: 0.8, 0.15: 0.64, 0.16: 0.56, 0.17: 0.8, 0.18: 0.6, 0.19: 0.6, 0.2: 0.68, 0.21: 0.6, 0.22: 0.6, 0.23: 0.66, 0.24: 0.58, 0.25: 0.6, 0.26: 0.6, 0.27: 0.6, 0.28: 0.8, 0.29: 0.6, 0.3: 0.6, 0.31: 0.6, 0.32: 0.6, 0.33: 0.6, 0.34: 0.6, 0.35: 0.6, 0.36: 0.6, 0.37: 0.6, 0.38: 0.6, 0.39: 0.8, 0.4: 0.6, 0.41: 0.6, 0.42: 0.6, 0.43: 0.8, 0.44: 0.6, 0.45: 0.6, 0.46: 0.6, 0.47: 0.66, 0.48: 0.8, 0.49: 0.6, 0.5: 0.6, 0.51: 0.6, 0.52: 0.8, 0.53: 0.48, 0.54: 0.6, 0.55: 0.6, 0.56: 0.6, 0.57: 0.6, 0.58: 0.6, 0.59: 0.8, 0.6: 0.6, 0.61: 0.8, 0.62: 0.8, 0.63: 0.6, 0.64: 0.6, 0.65: 0.6, 0.66: 0.6, 0.67: 0.6, 0.68: 0.6, 0.69: 0.76, 0.7: 0.46, 0.71: 0.76, 0.72: 0.6, 0.73: 0.6, 0.74: 0.6, 0.75: 0.6, 0.76: 0.6, 0.77: 0.6, 0.78: 0.6, 0.79: 0.6, 0.8: 0.8, 0.81: 0.6, 0.82: 0.8, 0.83: 0.8, 0.84: 0.8, 0.85: 0.8, 0.86: 0.72, 0.87: 0.8, 0.88: 0.76, 0.89: 0.6, 0.9: 0.6, 0.91: 0.6, 0.92: 0.6, 0.93: 0.6, 0.94: 0.6, 0.95: 0.6, 0.96: 0.6, 0.97: 0.6, 0.98: 0.6, 0.99: 0.6})