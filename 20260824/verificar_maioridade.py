class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def maioridade(self):
        if self.idade < 18:
            return False

        return True

fulano = Pessoa('fulano', 16)
print(f"É maior de idade: {fulano.maioridade()}")

gustavo = Pessoa('Gustavo', 18)
print(f"{gustavo.nome} é maior de idade: {gustavo.maioridade()}")