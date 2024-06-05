import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def gauss_seidel(coeficientes, terminos, aproximacion_inicial=None, tolerancia=0.000001, max_iteraciones=100):
    n = len(terminos)
    if aproximacion_inicial is None:
        aproximacion_inicial = np.zeros(n)
    solucion = aproximacion_inicial.copy()
    for _ in range(max_iteraciones):
        for i in range(n):
            solucion[i] = (terminos[i] - np.dot(coeficientes[i, :i], solucion[:i]) - 
                           np.dot(coeficientes[i, i + 1:], solucion[i + 1:])) / coeficientes[i, i]
        if np.linalg.norm(solucion - aproximacion_inicial) < tolerancia:
            break
        aproximacion_inicial = solucion.copy()
    return solucion.tolist()

coeficientes = np.array([[4, -1, 0],[-1, 4, -1],[0, -1, 3]])
terminos = np.array([15, 10, 10])

# Solución utilizando Gauss-Seidel
solucion = gauss_seidel(coeficientes, terminos)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Vector solución
x, y, z = solucion

# Origen del vector
origen = [0, 0, 0]

ax.quiver(origen[0], origen[1], origen[2], x, y, z, color='r')

ax.set_xlabel('Eje X'); ax.set_ylabel('Eje Y'); ax.set_zlabel('Eje Z')

# Título
ax.set_title('Vector solución del sistema de ecuaciones')

limite_max = max(x, y, z)
ax.set_xlim([0, limite_max])
ax.set_ylim([0, limite_max])
ax.set_zlim([0, limite_max])

plt.show()
