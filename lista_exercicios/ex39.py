# CRIAR UMA FUNÇÃO QUE RECEBA UMA LISTA DE NÚMEROS E RETORNE O MAIOR E O MENOR VALOR ENTRE ELES:
def maior_menor(valores):
    maior = max(valores)
    menor = min(valores)
    return f"O maior valor é:{maior}\nE o menor valor é: {menor}"

entrada = input("Digite alguns valores: ")
numeros = list(map(float, entrada.split()))

print(maior_menor(numeros))