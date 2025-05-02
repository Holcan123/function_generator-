#imports
import matplotlib.pyplot
import numpy  
import random
import matplotlib

#lists 
LC=random.randint(2,10)
constantes=random.sample(range(1,10),LC)  #bug going on because "sample is larger than population or negative" this needs to be fixed af it happends whuen LC==10 the order in with those numbers are order it gives their power 
polinomio=numpy.poly1d(constantes)             


#display plotted line  

X=numpy.linspace(-10,10,30) #defining linear spaces of point in x and then generating y values based on the polynommial class of numpy
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