from collections import OrderedDict

n = OrderedDict()
n['One'] = 'uno'
n['two'] = 'dos'
n['trhee'] = 'tres'

print(n)

#COMPARACION CON DICCIONARIOS NORMALES
n1 = {}
n1['uno'] = 'one'
n1['dos'] = 'two'

n2 = {}
n2['dos'] = 'two'
n2['uno'] = 'one'

# ¿Tienen los mismos elementos y en el mismo orden?
print(n1 == n2)

n1 = OrderedDict()
n1['uno'] = 'one'
n1['dos'] = 'two'

n2 = OrderedDict()
n2['dos'] = 'two'
n2['uno'] = 'one'

# ¿Tienen los mismos elementos y en el mismo orden?
print(n1 == n2)