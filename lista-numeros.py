lista = []

while True: #loop infinito - break pra travar
    n = int(input("Digite o numero desejado (0 para parar): "))

    if n == 0:
      break

    lista.append(n)

print(lista)