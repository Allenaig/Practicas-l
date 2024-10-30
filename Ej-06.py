#pip install torch

import torch
import numpy as np
import torch.nn as nn

# Crear un tensor a partir de una lista
tensor_a = torch.tensor([1, 2, 3, 4])

# Crear un tensor a partir de una matriz NumPy
import numpy as np
numpy_array = np.array([[1, 2], [3, 4]])
tensor_b = torch.tensor(numpy_array)

# Operaciones matemáticas
result = tensor_a + tensor_b

# Funciones de activación
sigmoid_output = torch.sigmoid(tensor_a)

# Manipulaciones de forma
reshaped_tensor = tensor_b.view(1, 4)

# Definir la arquitectura de la red neuronal
class NeuralNetwork(nn.Module):
def __init__(self):
super(NeuralNetwork, self).__init__()
self.fc1 = nn.Linear(784, 128)
self.fc2 = nn.Linear(128, 10)
def forward(self, x):
x = torch.flatten(x, 1)
x = self.fc1(x)
x = torch.relu(x)
x = self.fc2(x)
return x

# Instanciar la red neuronal
model = NeuralNetwork()