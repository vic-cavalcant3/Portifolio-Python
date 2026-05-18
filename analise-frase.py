frase = input("Digite uma frase desejada: ")

espacos_branco = frase.count(" ")
ponto_final = frase.endswith(".")

print(f"Espaços em branco: {espacos_branco}")

if ponto_final != 0:
   print("Esse texto tem ponto final!!")
else:
  print("Esse texto NÃO tem pronto!!")