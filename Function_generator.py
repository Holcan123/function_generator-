#imports
import numpy  
import random

LC=random.randint(1,10)
constantes=random.sample(range(1,10),LC)  #bug going on because "sample is larger than population or negative" this needs to be fixed af it happends whuen LC==10

                                                #the order in with those numbers are order it gives their power 

polinomio=numpy.poly1d(constantes)       
        
print(LC)
print(constantes)



print(polinomio)