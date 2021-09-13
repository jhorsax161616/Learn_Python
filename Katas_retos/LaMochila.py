def morral(tamano_morral, pesos, valores, n):
    print(0)
    if n == 0 or tamano_morral == 0:
        return 0
    if pesos[n - 1] > tamano_morral:
        return morral(tamano_morral, pesos, valores, n- 1)
    return max(valores[n-1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n-1),
                morral(tamano_morral, pesos, valores, n - 1))


if __name__ == '__main__':
    valores = [300, 10, 30, 20]
    pesos = [10, 20, 30, 20]
    tamano_morral = 50
    n = len(valores)
    repetidas = 0
    resultados = morral(tamano_morral, pesos, valores, n)

    print(resultados)
    print(repetidas)
