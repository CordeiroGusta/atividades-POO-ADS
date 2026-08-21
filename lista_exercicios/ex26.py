# LER UMA PALAVRA E CONTAR QUANTAS VOGAIS ELA TEM
vogais = ['a', 'e', 'i', 'o', 'u']
entrada = input("Digite uma palavra: ")
caracteres = [char for char in entrada if char != ' ']

vogais_palavra = 0
for i in caracteres:
    if i in vogais:
        vogais_palavra += 1

print(f"A palavra digitada possuí {vogais_palavra} vogais")