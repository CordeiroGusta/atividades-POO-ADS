# CRIE UMA FUNCAO QUE CALCULE O FATORIAL DE UM NUMERO

def fatorial(numero: int):
    """Recebe um número e calcula o fatorial dele"""
    if numero < 0:
        return "Não existe o fatorial de um número negativo"
    
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i

    return fatorial

numero = int(input("Digite um número: "))
print(f"O fatorial de {numero}, é: {fatorial(numero)}")
