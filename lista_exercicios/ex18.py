#LER A MEDIA FINAL DE UM ALUNO E INFORMAR SE ELE ESTA APROVADO, EM RECUPERAÇÃO, OU REPROVADO
media = float(input("Digite a média do aluno: "))

if media >= 7.0:
    print("O aluno foi Aprovado!")
elif media <= 6.9 and media >= 5:
    print("O aluno esta em recuperação!")
else:
    print("O aluno esta reprovado!")