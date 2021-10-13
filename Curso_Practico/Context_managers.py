#Example 1 --> Armando nuestro propio with open
class Abrir(object):
    def __init__(self, archivo):
        self.archivo = open(archivo, 'r')
    
    def __enter__(self):
        return self.archivo
    
    def __exit__(self, type, value, traceback):
        #print("Error de funcion con el archivo!!!")
        self.archivo.close()
        return True

try:
    with Abrir('file.txt') as f:
        #Usando a proposito una función inválida
        #linea = f.lip_d()
        linea = f.readline()
except:
    print("No se encontró el archivo")

#Example 2--> Utilizando el modulo contexlib
from contextlib import contextmanager

@contextmanager
def abrir(archivo):
    f = open(archivo, 'r')

    try:
        yield f
    finally:
        f.close()

try:    
    with abrir('file.txt') as f:
        line = f.readline()
except:
    print("No existe el archivo")