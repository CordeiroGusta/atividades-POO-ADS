#Exercicio 02

n1, n2, n3, n4 = list(map(float, input("Digite quatro notas: ").split()))

media = (n1 + n2 + n3 + n4) / 4

if media >= 6.0:
    print(f"Sua média foi {media:.1f}\nVocê foi aprovado!")
elif media <= 5.9 and media >= 4.0:
    print(f"Sua média foi {media:.1f}\nVocê esta de recuperação!")
else:
    print(f"Sua média foi {media:.1f}\nVocê foi reprovado!")