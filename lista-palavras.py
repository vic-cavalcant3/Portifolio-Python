palavras = input("Digite palavras separadas por espaço: ").split()
novas_palavras = input("Digite mais palavras para adicionar: ").split()

palavras.extend(novas_palavras) # múltiplos itens de uma vez no final
print("Lista Completa:", palavras)