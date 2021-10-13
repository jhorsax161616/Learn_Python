#Examples
try:
    resul = 5/0
except ZeroDivisionError:
    print('No se puede dividir entre cero..!')

try:
    a = 'hola'
    result = 5 + a
except TypeError:
    print('No se puede sumar!!!')
