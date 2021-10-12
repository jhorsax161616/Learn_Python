#Example 1
def decora(funcion):
    def wrapper():
        print('mi ultimo mensaje....')
        funcion()
        print('Este es el primer mensaje ;)')
    return wrapper

@decora
def zumbido():
    print('zzzzzzzz')


#Example 2
PASSWORD = '12345'

def password_required(func):
    #por convención llamamos wrapper a la función interna (decorador)
    def wrapper():
        password = input('Ingrese contraseña: ')
        if password == PASSWORD:
            return func()
        else:
            print('La conraseña no es correcta!')
    
    return wrapper

@password_required
def needs_password():
    print('La contraseña es correcta!')

#Example 3
def upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        return result.upper()
    
    return wrapper

@upper
def say_my_name(name):
    return f'Hola, {name}'

if __name__=='__main__':
    print()
    zumbido()
    print()
    needs_password()
    print()
    print(say_my_name('jhorsax'))