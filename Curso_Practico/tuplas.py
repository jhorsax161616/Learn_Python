tupl = (1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 4)

print(tupl)
#contando cuantas veces aparece un valor
print("tupl.count(1) -->  " + tupl.count(1)) ##--> 5
print("tupl.count(2) -->  " + tupl.count(2))
print("tupl.count(3) -->  " + tupl.count(3))

#Indice de la primera aparicion de ese valor
print("tupl.index(1) -->  " + tupl.index(1))
print("tupl.index(3) -->  " + tupl.index(3))
print("tupl.index(4) -->  " + tupl.index(4))

print('\n\n')
#SETS
#Utilizados generalmente para trabajar con diagramas de euler
#Formas de declarar un set
a = set([1, 2, 3])
b = {3, 4, 5}

print(a)
print(b)
#Estos objetos no pueden tener elementos repetidos

a.add(3)
print(a) #no se va a modificar ya que tenemos el elemento 3 en el set

a.add(15)
print(a) #si se añade el 15 ya que no es un elemento repetido

#Intersecciones
print(a.intersection(b))

#union
print(a.union(b))

#diferencia
print(a.difference(b))
print(b.difference(a))

##Borrando elementos
a.remove(15)
b.remove(4)

print("Metodos que se puede trabajar con sets")
print(dir(a))