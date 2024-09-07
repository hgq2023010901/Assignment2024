import numpy as np

class NeuralNetwork:
    def __init__(self, layers):
        self.layers = layers
        self.weights = [np.random.randn(self.layers[i+1], self.layers[i]) for i in range(len(self.layers)-1)]
        self.biases = [np.random.randn(self.layers[i+1]) for i in range(len(self.layers)-1)]

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def forward_propagation(self, X):
        for w, b in zip(self.weights, self.biases):
            X = self.sigmoid(np.dot(w, X) + b.reshape(len(b), 1))
        return X

if __name__ == "__main__":
    layers = input("Enter the number of neurons in each layer: ").split()
    layers = [int(i) for i in layers]
    nn = NeuralNetwork(layers)
    X = input("Enter the input values: ").split()
    X = [float(i) for i in X]
    X = np.array(X).reshape(len(X), 1)
    output = nn.forward_propagation(X)
    print("Output of the neural network:", output)