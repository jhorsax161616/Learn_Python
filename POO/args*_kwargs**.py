#example 1
def sum(*args):
    suma = 0
    for i in args:
        suma += i
    return suma

#example 2
def filter(**kwargs):
    consulta = "SELECT * FROM clientes"
    i=0
    for key, value in kwargs.items():
        if i == 0:
            consulta += " WHERE "
        else:
            consulta += " AND "
        consulta += f"{key}='{value}'"
        i +=1
    consulta += ";"

    return consulta

#example3
def resultado(x, y, op):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y



if __name__=='__main__':
    print(sum(1, 2))
    print(sum(1, 2, 3))
    print(sum(2, 4, 6, 8, 7, 9))

    print()

    print(filter())
    print(filter(ciudad="Lima"))
    print(filter(ciudad="Huancayo", fecha = "15-03-2015"))

    print()

    print(resultado(3, 5, '+'))

    #con un iterable
    it = (3, 5, '+')
    print(resultado(*it))

    it = (1, 2)
    print(resultado(*it, '-'))

    #con un diccionario
    it = {"op": "-", "y": 6, "x":3}
    print(resultado(**it))