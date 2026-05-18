senha = "python123"

while True:
  t = input("Digite a tentativa da senha: ")
  if t != senha:
    print("Senha Incorreta!!, tente novamente.")
  else:
    print("Senha Correta!!")
    break