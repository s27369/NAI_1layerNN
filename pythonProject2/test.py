import os
import re
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
if __name__ == '__main__':
    # create_folders(test_folder, languages)
    # create_files(test_folder, "testfile")
    clean_text(test_folder, "testfile")
    get_text_lengths(test_folder, "angielski", "testfile")
    get_text_lengths(test_folder, "polski", "testfile")
    language_stats(test_folder, "testfile")