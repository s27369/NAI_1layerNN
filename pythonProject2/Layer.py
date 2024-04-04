from Perceptron import *

class Layer:
    def __init__(self, num_inputs, languages, learning_rate,bias):
        self.neurons = {lang:Perceptron(num_inputs, learning_rate, bias) for lang in languages}

    def train_layer(self, dataset):
        for lang, neuron in self.neurons.items():
