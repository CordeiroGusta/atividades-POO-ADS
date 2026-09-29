class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def aprovado(self):
        return self.nota >= 7

aluno1 = Aluno("Gustavo", 8)
aluno2 = Aluno("Felipe", 4)

print(f"{aluno1.nome} foi aprovado? {aluno1.aprovado()}")
print(f"{aluno2.nome} foi aprovado? {aluno2.aprovado()}")