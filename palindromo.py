palavra = input("Digite a palavra: ")

palavra = palavra.strip()
palavra = palavra.lower()
tamanho = palavra.count("") -1

palindromo = True

for i in range(tamanho):
  if palavra[i] != palavra[tamanho - 1 - i]:
    palindromo = False
    break

if palindromo == True:
  print("A palavra é um Palindromo")
else:
  print("A palavra não é um Palindromo")