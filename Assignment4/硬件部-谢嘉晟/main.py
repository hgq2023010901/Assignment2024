# main.py
import numpy as np
from neural_network import NeuralNetwork

# 创建数据集（逻辑与操作）
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [0], [0], [1]])  # 逻辑与的输出

# 初始化神经网络：2输入，2隐藏层神经元，1输出
nn = NeuralNetwork(input_size=2, hidden_size=2, output_size=1)

# 训练神经网络
nn.train(X, y, epochs=10000)

# 打印训练后的预测结果
print("预测结果:")
print(f"Input: [0, 0], Predicted Output: {nn.predict(np.array([[0, 0]]))}")
print(f"Input: [0, 1], Predicted Output: {nn.predict(np.array([[0, 1]]))}")
print(f"Input: [1, 0], Predicted Output: {nn.predict(np.array([[1, 0]]))}")
print(f"Input: [1, 1], Predicted Output: {nn.predict(np.array([[1, 1]]))}")
