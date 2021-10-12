from collections import defaultdict

d = defaultdict(float)  # tipo flotante por defecto
print(d['algo'])
print(d)

d = defaultdict(str)  # tipo cadena por defecto
print(d['algo'])
print(d)

d = defaultdict(object)  # tipo objeto por defecto
print(d['algo'])
print(d)