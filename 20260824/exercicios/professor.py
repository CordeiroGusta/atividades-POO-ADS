class Professor:
    def __init__(self, nome, disciplina):
        self.nome = nome
        self.disciplina = disciplina

    def apresentar(self):
        return f"Meu nome é {self.nome}, e eu ensino {self.disciplina}"

entrada_nome = input("Digite o seu nome: ")
entrada_disciplina = input("Digite a sua disciplina: ")

professora = Professor(entrada_nome, entrada_disciplina)
print(professora.apresentar())