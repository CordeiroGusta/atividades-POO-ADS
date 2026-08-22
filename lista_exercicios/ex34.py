# CRIE UMA FUNÇÃO QUE RECEBE DOIS NUMEROS E RETORNA A SOMA ENTRE ELES
def soma(a, b: float):
    """Recebe dois números e retorna a soma entre eles"""
    return a + b

a = float(input("Digite um valor: "))
b = float(input("Digite outro valor: "))
print(f"A soma entre os valores é: {soma(a, b)}")