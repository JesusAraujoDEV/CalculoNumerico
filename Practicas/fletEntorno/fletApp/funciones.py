import numpy as np

def fromDEC(n, base):
    """Convierte un número decimal en una cadena en el sistema de base especificada."""
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(int(n), base)
        nums.append(str(r))
    return ''.join(reversed(nums))

def toDEC(n, base):
    """Convierte una cadena en el sistema de base especificada en un número decimal."""
    return str(int(n, base))

def creacionMatriz(n, lista):
    """
    Crea una matriz cuadrada de tamaño n a partir de una lista de elementos.
    
    Si la lista tiene menos elementos que los necesarios para formar una matriz cuadrada de tamaño n,
    la función devuelve None.
    """
    if len(lista) > n**2:
        pass
    else:
        matriz = np.array(lista[:n**2]).reshape(n, n)
        return matriz

def creacionVector(n, lista = []):
    """
    Crea un vector de tamaño n a partir de una lista de elementos.
    
    Si no se proporciona una lista, la función crea un vector de ceros.
    """
    if len(lista) == 0:
        lista = [0.0 for i in range(n)] 
    return np.array(lista[:n])

def GaussSeidel(a, b, x0=None, tol=0.000001, max_ite=100):
    """
    Resuelve un sistema de ecuaciones lineales usando el método de Gauss-Seidel.

    Args:
        a (numpy.ndarray): Matriz de coeficientes.
        b (numpy.ndarray): Vector de términos constantes.
        x0 (numpy.ndarray, opcional): Aproximación inicial. Si no se proporciona, se utiliza un vector de ceros.
        tol (float, opcional): Tolerancia para la convergencia.
        max_ite (int, opcional): Número máximo de iteraciones permitidas.

    Returns:
        list: Lista con la solución del sistema de ecuaciones.
    """
    n = len(b)
    if x0 is None:
        x0 = np.zeros(n)
    x = x0.copy()
    for _ in range(max_ite):
        for i in range(n):
            x[i] = (b[i] - np.dot(a[i, :i], x[:i]) - np.dot(a[i, i + 1:], x[i + 1:])) / a[i, i]
        if np.linalg.norm(x - x0) < tol:
            break
        x0 = x.copy()
    return x.tolist()
