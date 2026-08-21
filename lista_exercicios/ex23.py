# SORTEAR UM NUMERO E PEDIR PRO USER DIGITAR
from random import randint

palpite = 0
numero_sorteado = randint(1,100)

while palpite != numero_sorteado:
    print("\nTente advinhar o número sorteado!")
    palpite = int(input("Digite seu palpite: "))

    if palpite < numero_sorteado:
        print("O seu palpite foi maior que o número sorteado! Tente novamente")
    elif palpite > numero_sorteado:
        print("O seu palpite foi menor que o número sorteado! Tente novamente")
    else:
        print(f"Você acertou!! O numero sorteado era {numero_sorteado}")
        break