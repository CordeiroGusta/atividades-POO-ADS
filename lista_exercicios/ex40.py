# CRIAR UMA FUNÇÃO RECURSIVA QUE RETORNE A SEQUÊNCIA DE FIBONNACI DA POSIÇÃO INFORMADA
def fibonacci(posicao):
    if posicao == 0:
        return 0

    if posicao == 1:
        return 1

    return fibonacci(posicao - 2) + fibonacci(posicao - 1)

valor = int(input("Digite um valor: "))
print(f"O valor da sequência de Fibonacci para o valor informado é: {fibonacci(valor)}")