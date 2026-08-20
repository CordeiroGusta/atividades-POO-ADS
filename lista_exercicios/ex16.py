#LER TRÊS NUMEROS E EXIBIR O MAIOR DELES
entrada = input("Digite três números: ")

numeros = list(map(float, entrada.split()))

print(f"O maior número é: {max(numeros)}")