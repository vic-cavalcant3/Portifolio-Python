numero = int(input("Digite um numero inteiro: "))

numero_primo = True

# números menores que 2 não são primos
if numero < 2:
  numero_primo = False
else:
  # números menores que 2 não são primos
  for i in range(2, numero):
    if numero % i == 0: # 0 = divisor
      numero_primo = False #divisor = PrimoFalse
      break

if numero_primo:
    print(f"{numero} É um número primo.")
else:
    print(f"{numero} NÃO é um número primo.")