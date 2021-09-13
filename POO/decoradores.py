def decora(funcion):
    def wrapper():
        print('mi ultimo mensaje....')
        funcion()
        print('Este es el primer mensaje ;)')
    return wrapper()

@decora
def zumbido():
    print('zzzzzzzz')
