senha = "123senai"

while True:
  t = input("Digite a tentativa da senha: ")
  if t != senha:
    print("Senha Incorreta!!, tente novamente.")
  else:
    print("=" * 40)
    print("Senha Correta!! Acesso Liberado!!")
    print("=" * 40)
    break

numero = int(input("Digite um numero de 1 a 10: "))

if numero < 1 or numero > 10:
  print("Numero fora de 1 a 10!")
else:
  print("=" * 40)
  print(f"Tabuada do {numero}: \n")

  if numero % 2 == 0: #multiplicadores pares
    for i in range(2,11,2):
      print(f"{numero} x {i} = {numero * i}")
  else:
    for i in range(1,10,2):
      print(f"{numero} x {i} = {numero * i}")