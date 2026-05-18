while True:
  nome = input("Digite seu nome: ")

  valido = True
  for letra in nome:
      if letra != " " and not letra.isalpha(): #verifica se todos são letras
        valido = False

  if not valido:
    print("Nome Invalido!! Escreva apenas letras e espaços.")
  else:
    break

nome = nome.strip()
nome = nome.title()

hora = int(input("Digite a hora atual (ex: 8 ou 14 ou 22): "))

if 5 <= hora <= 11: #encadeamento de condição
  saudacao = "bom dia"
elif 12 <= hora <= 17:
  saudacao = "boa tarde"
else:
  saudacao = "boa noite"

print("=" * 40)
print(f" {saudacao}, {nome}!")
print(f" Seja Bem-Vindo(a), {nome}!")
print("=" * 40)
