n1 = int(input("Digite o PRIMEIRO numero: "))
n2 = int(input("Digite o SEGUNDO numero: "))

def verificar_par_impar(numero):
  if numero % 2 == 0:
    print("O Resultado é par")
  else:
    print("O Resultado é impar")

def verificar_positivo_negativo(numero):
  if numero > 0:
    print("O numero é positivo")
  elif numero < 0:
    print("O numero é negativo")
  else:
    print("O resultado é zero")

def verificar_inteiro_decimal(numero):
  if numero == int(numero):
    print("O numero é inteiro!")
  else:
    print("O numero é decimal!")

def operacao(n1, n2):
  print("===== CALCULADORA =====")
  print("1 - Soma")
  print("2 - Subtração")
  print("3 - Divisão")
  print("4 - Multiplicação")
  escolha = int(input("Qual Operação você deseja?? "))

  if escolha == 1:
      resultado = n1 + n2
  elif escolha == 2:
      resultado = n1 - n2
  elif escolha == 3:
      resultado = n1 / n2
  elif escolha == 4:
      resultado = n1 * n2
  else:
      print("OPÇÃO INVÁLIDA!")
      return
  print(f"\nResultado: {resultado}")

  verificar_par_impar(resultado)
  verificar_positivo_negativo(resultado)
  verificar_inteiro_decimal(resultado)

operacao(n1,n2)