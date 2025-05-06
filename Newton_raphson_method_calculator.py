import numpy
import matplotlib.pyplot
from Function_generator import polinomio, X, Y

def calculate_tangent_line(polinomio, x0, y0):
    # Calcular la derivada del polinomio
    polynomial_derivative = numpy.polyder(polinomio)
    
    # Evaluar la pendiente (m) en x0
    m = numpy.polyval(polynomial_derivative, x0)
    
    # Definir la ecuación de la tangente: y = m * (x - x0) + y0
    tangent_line = lambda x: m * (x - x0) + y0
    
    return tangent_line

# Función para graficar la línea tangente
def plot_tangent_line(x0, y0):
    tangent_line = calculate_tangent_line(polinomio, x0, y0)
    
    # Generar puntos para la línea tangente
    X_tangent = numpy.linspace(min(X), max(X), 100)
    Y_tangent = tangent_line(X_tangent)
    
    # Graficar la función original y la tangente
    matplotlib.pyplot.figure(figsize=(10, 10))
    matplotlib.pyplot.plot(X, Y, label="Función Original", color="blue")
    matplotlib.pyplot.plot(X_tangent, Y_tangent, label=f"Tangente en x0={x0:.2f}", color="red", linestyle="--")
    matplotlib.pyplot.scatter([x0], [y0], color="green", label=f"Punto Seleccionado ({x0:.2f}, {y0:.2f})")
    matplotlib.pyplot.grid(True)
    matplotlib.pyplot.legend()
    matplotlib.pyplot.show()
