def fibonacci(n):
    print(n)
    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

result = fibonacci(int(input('Ingresa el mes: ')))

print(result)
