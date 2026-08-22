#CRIAR UMA LISTA COM 5 NÚMEROS DIGITADOS PELO USER E EXIBA O MAIOR E O MENOR
entrada = input("Digite alguns valores: ")
numeros = list(map(float, entrada.split()))

print(f"O maior valor digitado é: {max(numeros)}\nO menor valor digitado: {min(numeros)}")