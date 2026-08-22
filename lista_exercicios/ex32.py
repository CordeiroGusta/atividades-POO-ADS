# CRIAR UMA LISTA DE NÚMEROS E CALCULAR A SOMA DELES
entrada = input("Digite alguns valores: ")
numeros = list(map(float, entrada.split()))

print(f"A soma dos elementos: {sum(numeros)}")