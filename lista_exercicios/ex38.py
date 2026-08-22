# CRIAR UMA FUNÇÃO soma() QUE PODE RECEBER INUMEROS PARÂMETROS
def soma(*numeros):
    return sum(numeros)

numeros = []
print("Digite valores abaixo ou aperte enter para encerrar")
while True:
    entrada = input("Valor: ")

    if entrada == '' or entrada is None:
        break
    else:
        valor = float(entrada)
        numeros.append(valor)

print(f"A soma dos números digitados é: {soma(*numeros)}")