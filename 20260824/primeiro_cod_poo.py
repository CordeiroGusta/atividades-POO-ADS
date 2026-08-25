class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# class Usuario(Pessoa):
#     def __init__(self, id, nome, login):
#         super().__init__(nome)
#         self.Pessoa.nome = nome
#         self.id = id
#         self.login = login
    
# ENCAPSULAMENTO
'''
Quando chamamos os atributos de uma classe, e criamos um novo objeto, com novos valores, apartir dessa classe
'''
pessoa1 = Pessoa('Gustavo', 19)
print(pessoa1.nome)

pessoa2 = Pessoa("Ana", 21)
print(f"Nome: {pessoa2.nome}\nIdade: {pessoa2.idade}")

# usuario = Usuario(12, 'felipleins', 'raycicles@dotmail.com')
# print(usuario.id)

'''
Realmente o __init__ funciona como um construtor, eu posso chamar ele a  qualquer hora e criar um novo objeto, que possuí os mesmos atributos
'''