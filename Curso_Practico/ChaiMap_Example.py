import collections

#ChainMap -> Util para crear plantillas   Example
antes = {'a': 'A', 'c': 'C'}
nuevo = {'b': 'B', 'c' : 'D'}

resul = collections.ChainMap(antes, nuevo)

print("\t_Resultado_")
print(f'Keys = {list(resul.keys())}')
print(f'Values = {list(resul.values())}')

print()
print('Items:')
for k, v in resul.items():
    print('{} = {}'.format(k, v))
print()

print(resul.maps)

###Podemos revertir
resul.maps = list(reversed(resul.maps))
print(resul.maps)

##Actualizando valores (Ojo: Se invirtió la prioridad en la sección anterior)
print()
print(f'Keys = {list(resul.keys())}')
print(f'Values = {list(resul.values())}')
nuevo['c'] = 'X'
print()
print(f'Keys = {list(resul.keys())}')
print(f'Values = {list(resul.values())}')