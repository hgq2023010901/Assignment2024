import numpy as np

class NeuralNetwork:  
    def __init__(self, layer_sizes):  
        #初始化神经网络
        #layer_sizes储存每层的神经元数量
        self.layer_sizes = layer_sizes  
        self.num_layers = len(layer_sizes)  
        self.weights = []  
        self.biases = []  
        
        #初始化权重和偏置  
        for i in range(self.num_layers - 1):  
            weight_matrix = np.random.randn(layer_sizes[i], layer_sizes[i + 1])  
            bias_vector = np.random.randn(layer_sizes[i + 1])  
            self.weights.append(weight_matrix)  
            self.biases.append(bias_vector)  
    
    #激活函数sigmoid
    def sigmoid(self, z):  
        return 1 / (1 + np.exp(-z))  
    
    #正向传播
    def forward(self, x):  
        #输入数据x
        res = x  
        for i in range(self.num_layers - 1):  
            z = np.dot(res, self.weights[i]) + self.biases[i]  
            res = self.sigmoid(z)  
        return res  

#测试
# 输入层有3个神经元，隐藏层有4个神经元，输出层有2个神经元
layer_sizes = [3, 4 ,2]
#创建神经网络
nn = NeuralNetwork(layer_sizes)
#随机输入数据
input = np.random.randn(3)
#向前传播输出结果
output = nn.forward(input)
print("Output od the neural network: ", output)