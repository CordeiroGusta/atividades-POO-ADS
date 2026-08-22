# LEIA UMA PALAVRA E RETORNE SE ELA É UM PALINDROMO (SE LE DA MESMA FORMA AO CONTRARIO)
entrada = input("Digite uma palavra: ")
palavra = [char for char in entrada if char != '']

palavra.reverse()
palavra_inversa = "".join(palavra)

if entrada == palavra_inversa:
    print("A palavra digitada é um Palíndromo")
else:
    print("A palavra digitada não é Palíndromo")