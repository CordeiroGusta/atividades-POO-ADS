# LER AS DUAS NOTAS DE UM ALUNO E CALCULE A MEDIA ARITMETICA DE UM ALUNO
entrada = input("Digite as duas notas do aluno: ")
notas = list(map(float, entrada.split()))
media = (notas[0] + notas[1]) / len(notas)

print(f"A média é: {media}")