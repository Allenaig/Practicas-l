#pip install scikit-learn
#python Ej-06.py

import sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Cargar el conjunto de datos Iris
iris = load_iris()
X, y = iris.data, iris.target

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear un modelo de regresión logística
model = LogisticRegression()

# Entrenar el modelo en los datos de entrenamiento
model.fit(X_train, y_train)

# Calcular la precisión del modelo en los datos de prueba
accuracy = model.score(X_test, y_test)
print("Precisión del modelo:", accuracy)

# Hacer predicciones sobre nuevos datos
new_data = [[5.1, 3.5, 1.4, 0.2], [6.2, 2.8, 4.8, 1.8]]
predictions = model.predict(new_data)
print("Predicciones:", predictions)