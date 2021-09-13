def factorial(n):
	"""Factorial de n
	int n > 0
	returns n!"""
	if n == 1:
		return 1
	return n * factorial(n - 1)
	

number = int(input('Ingresa un número: '))

resultado = factorial(number)

print(resultado)

