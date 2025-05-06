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
    X_tangent = numpy.linspace(0, max(X), 20)
    Y_tangent = tangent_line(X_tangent)
    return X_tangent, Y_tangent,m


def NRM(polinomio, x0):
    for i in range(20):
        # Evaluate the function value f
        fx = numpy.polyval(polinomio, x0)
        
        # Calculate the derivative uwu
        polynomial_derivative = numpy.polyder(polinomio)
        f_prime_x = numpy.polyval(polynomial_derivative, x0)
        
        # check if derivative is 0 because whuen you divide by 0 computers explode 
        if f_prime_x == 0:
            print(i + 1)
            return None
        
        #NRF formula (thanks newton and Raphson)
        x1 = x0 - (fx / f_prime_x)        
        
        x0 = x1
    
    # FINAL RESULT 
    print(f"final rslt  {x0}:")
    return x0

