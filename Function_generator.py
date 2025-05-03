#imports
import matplotlib.pyplot
import numpy  
import random
import matplotlib

#lists 
LC=random.randint(1,10) #LC= leading coeficient 
constantes=random.sample(range(1,11),LC)  #bug going on because this needs to be fixed af it happends whuen LC==10 the order in with those numbers are order it gives their power 
polinomio=numpy.poly1d(constantes)             


#display plotted line  

X=numpy.linspace(-10,10,100) #defining linear spaces of point in x and then generating y values based on the polynommial class of numpy
Y=polinomio(X)


print(LC)
print(constantes)
print(polinomio)
print(X)
print(Y)


matplotlib.pyplot.figure(figsize=(10,10))
matplotlib.pyplot.plot(X,Y)
matplotlib.pyplot.grid(True)
matplotlib.pyplot.show()