from collections import Counter

#Contando elementos repetidos en una lista
l = [1, 2, 3, 4, 1, 2, 3, 1, 2, 1]
print(Counter(l))

print()

#Contando elementos repetidos en una cadena
word = "ascinante"
print(Counter(word))

print()

frase = "el gran granero es el mas fascinante"
print(Counter(frase.split()))

##ALGUNAS UTILIDADES
animales = "gato perro canario perro canario perro"
c = Counter(animales.split())

print(c.most_common(1))  # Primeros elemento más repetido
print(c.most_common(2))  # Primeros dos elementos más repetidos
print(c.most_common())   # Elementos ordenadores por repeticiones

#Con listas
l = [10,20,30,40,10,20,30,10,20,10]
c = Counter(l)

print(c.items())        # Registros del contador por clave-valor
print(c.keys())         # Registros del contador por clave
print(c.values())       # Registros del contador por valor

print(sum(c.values()))  # Suma total de elementos del contador

print(list(c))          # Conversión a lista
print(dict(c))          # Conversión a conjunto
print(set(c))           # Conversión a conjunto