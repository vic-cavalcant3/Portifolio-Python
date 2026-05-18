lista = []


while True:
  frase = input("Digite uma frase (ou 'sair' para terminar): ")

  if frase.lower() == "sair":
    break

  lista.append(frase)

print("\nFrases com ponto final: ")

encontrou = 0

for frase in lista:
  if frase.endswith("."):
    print(f"{frase}")
    encontrou = 1

if encontrou == 0:
    print("Nenhuma frase termina com ponto final.")