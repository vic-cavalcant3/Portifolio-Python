n = int(input("Digite um numero: "))
fatorial = 1 # se ficasse 0 na multiplicação ia zerar tudo
i = 1

while i <= n:
    fatorial *= i  # fatorial = fatorial * i
    i += 1  # ex: 1*1=1, 1*2=2, 2*3=6, 6*4=24...

print(f"Fatorial de {n} = {fatorial}")