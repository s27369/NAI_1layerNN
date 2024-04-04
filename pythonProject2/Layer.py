from Perceptron import *

class Layer:
    def __init__(self, num_inputs, languages, learning_rate,bias):
        self.neurons = {lang:Perceptron(num_inputs, learning_rate, bias, lang) for lang in languages}

    def train_layer(self, dataset, epochs=0):
        counter = 1
        for lang, neuron in self.neurons.items():
            print(f"Neuron {counter} (language={lang}):")
            if epochs ==0: neuron.train(dataset)
            else: neuron.train(dataset, epochs)
            print("\n")
            counter+=1

    def predict(self, observation):
        p = []
        for lang, neuron in self.neurons:
            if neuron.predict(observation) == 1:
                p.append(lang)
        if len(p)>1:
            print(f"Conflict: possible languages={p}")
        if len(p)==0:
            print(f"error: didn't detect any language")
            return None
        return p[0]
