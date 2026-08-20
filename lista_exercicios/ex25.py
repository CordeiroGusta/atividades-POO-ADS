# LER O NOME COMPLETO DE UMA PESSOA E EXIBIR O PRIMEIRO NOME DA PESSOA
entrada = input("Digite seu nome completo: ")
nome_completo = list(map(str, entrada.split()))

print(f"Primeiro nome: {nome_completo[0]}")