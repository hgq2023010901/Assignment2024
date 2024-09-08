import numpy as np

class NeuralNetwork:
    def __init__(self, layer_sizes):
        #输入参数为层数的列表
        self.weights = []
        self.biases = []
        for i in range(len(layer_sizes) - 1):
            # 权重矩阵
            weight_matrix = np.random.randn(layer_sizes[i], layer_sizes[i + 1])
            # 偏置向量
            bias_vector = np.zeros((1, layer_sizes[i + 1]))
            self.weights.append(weight_matrix)
            self.biases.append(bias_vector)

    def sigmoid(self, x):
        """
        映射
        """
        return 1 / (1 + np.exp(-x))

    def forward(self, X):
        activation = X
        for weight, bias in zip(self.weights, self.biases):
            z = np.dot(activation, weight) + bias
            activation = self.sigmoid(z)
        return activation
    
if __name__ == "__main__":
    # 定义网络结构
    input_size = 2
    hidden_size = 3
    output_size = 2
    nn = NeuralNetwork([input_size, hidden_size, output_size])

    # 输入数据
    X = np.array([[0.5, 0.3]])
    
    # 前向传播
    output = nn.forward(X)
    print("Output:", output)