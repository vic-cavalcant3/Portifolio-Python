senha_certa = "victor25"
t = 0

while t < 3:
  senha = input("Digite a senha desejada: ")
  t += 1 # já incremento independente de acertar ou errar

  if senha == senha_certa:
    print("Senha correta! ")
    break
  else:
    tentativas = 3 - t

    if tentativas > 0:
      print(f"Senha errada! Tentativas Restantes: {tentativas} ")
    else:
      print("Senha errada! Número de tentativas acabou!!.")