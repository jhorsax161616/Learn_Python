from collections import namedtuple

People = namedtuple('People', 'name last_name age')
p = People("Sax", "Bach", 20)

print(p)
print()
#Accediendo a los elementos como atributos de un objeto
print(p.name)
print(p.age)

#O simplemente con indices
print()
print(p[0])
print(p[:3])

