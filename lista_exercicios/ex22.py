#LER A NOTA DE 5 ALUNOS E CALCULAR A MÉDIA DA TURMA
notas = []
for i in range(5):
    nota = float(input("Digite a nota de um aluno: "))
    notas.append(nota)

media_turma = sum(notas) / len(notas)
print(f"A media da sala é: {media_turma}")