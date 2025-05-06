#imports
import matplotlib.pyplot
import numpy  
import random
import matplotlib


#lists 
LC=random.randint(1,10) #LC= leading coeficient 
constantes=random.sample(range(1,11),LC)  
polinomio=numpy.poly1d(constantes)             


#display plotted line  

X=numpy.linspace(-10,10,100) #defining linear spaces of point in x and then generating y values based on the polynommial class of numpy
Y=polinomio(X)

print(LC)
print(constantes)
print(polinomio)
print(X)
print(Y)

#making the points on the graph selectable
def clickpoint(click):
    identifier=click.ind[0]
    x0 =X[identifier]
    y0 =Y[identifier]
 


#display plotted line 
matplotlib.pyplot.figure(figsize=(10,10))
matplotlib.pyplot.plot(X,Y, marker= 'o',picker=3)
matplotlib.pyplot.grid(True)
matplotlib.pyplot.gcf().canvas.mpl_connect('pick_event', clickpoint)   # this is pure black magic credits to random smart indian guy! i think that Retrieves the selected point of the current function and records its value when you click on it and does what the you tell the function to do! .
matplotlib.pyplot.show()