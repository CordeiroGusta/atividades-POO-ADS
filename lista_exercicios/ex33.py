# CRIAR UMA FUNÇÃO QUE RECEBA UM NOME COMO PARÂMETRO E RETORNE UMA MENSAGEM DE BOAS VINDAS
def saudacoes(nome: str):
    """recebe um nome e retorna uma mensagem de saudações personalizadas"""
    return f"Seja muito bem vindo senhor(a), {nome}, lorde do universo"

nome = input("Digite o seu nome: ")
print(saudacoes(nome))