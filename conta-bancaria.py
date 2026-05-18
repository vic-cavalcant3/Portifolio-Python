nome = input("Digite o seu nome: ")
conta = [nome, 0 ] # nome = [0]    //   saldo = [1]

def depositar():
  valor = float(input("Digite o valor do deposito: "))

  if valor <= 0:
    print("Valor Invalido!!")
  else:
    conta[1] += valor
    print(f"Deposito de {valor:.2f} feito com sucesso!!")

def sacar():
  valor = float(input("Digite o valor do saque: R$ "))
  if valor <= 0:
    print("Valor Invalido!!")
  elif valor > conta[1]: #saldo suficiente??
    print("Saldo Insuficiente!!")
  else:
    conta[1] -= valor
    print(f"Saque de R$ {valor:.2f} feito com sucesso!!")

def exibir_saldo():
  print("\n")
  print("=" * 40)
  print(f"Titular: {conta[0]}")
  print(f"Saldo: R$ {conta[1]:.2f}")
  print("=" * 40)

while True:
  print("\n=== BANCO ===")
  print("1 - Depósito")
  print("2 - Saque")
  print("3 - Exibir Saldo")
  print("4 - Sair")

  opcao = int(input("Digite uma opção: "))

  if opcao == 1:
      depositar()
  elif opcao == 2:
      sacar()
  elif opcao == 3:
      exibir_saldo()
  elif opcao == 4:
      print(f"Até a proxima!!, {conta[0]}!")
      break
  else:
      print("Opção inválida!")