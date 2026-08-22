# LEIA UMA PALAVRA E INVERTA A ORDEM DELA
entrada = input("Digite uma palavra: ")
palavra = [char for char in entrada if char != '']

palavra.reverse()
palavra_inversa = "".join(palavra)
print(palavra_inversa)