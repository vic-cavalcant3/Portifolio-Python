n = int(input("Digite um número inteiro positivo: "))

# primeiros parametros 0 e 1 são fixos!!
a = 0
b = 1

while a <= n:
    print(a, end=" ")  # end=" " printar na mesma linha separado por espaço

    # a vira o que era b
    # b vira a soma dos dois (proximo numero da sequencia)
    a, b = b, a + b