entrada = input("Digite os números separados por espaço: ")
numeros = entrada.split()
# print(numeros)

soma = 0
for numero in numeros:
  soma += int(numero)

media = soma / len(numeros)
print(f"Media: {media:.2f}")