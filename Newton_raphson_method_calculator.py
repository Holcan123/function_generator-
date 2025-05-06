import numpy

# Function to calculate the derivada
def calculate_tangent_line(polinomio, x0, y0, X):
    # Calculate the derivative of the polynomial
    polynomial_derivative = numpy.polyder(polinomio)
    
    # Evaluate the slope m at  the cordinate of x0
    m = numpy.polyval(polynomial_derivative, x0)
    
    # Define the tangent line equation ( y = m * (x - x0) + y0 )
    tangent_line = lambda x: m * (x - x0) + y0
    
    # Generate points for the tangent line
    X_tangent = numpy.linspace(min(X), max(X), 20)
    Y_tangent = tangent_line(X_tangent)
    return X_tangent, Y_tangent,m


def NRM(polinomio, x0, y0):
    # Calculate the derivative of the polynomial,also calculates the slope and if theres no intercept retunr nothuing 
    polynomial_derivative = numpy.polyder(polinomio)
    m = numpy.polyval(polynomial_derivative, x0)
    if m == 0:
        print("BRAH PICK A GOOD point like is not intercepting at nothing ggs")
        return None
    
    # Calculates the intercept :P
    x_intercept = x0 - (y0 / m)
    print(x_intercept)
    return x_intercept




