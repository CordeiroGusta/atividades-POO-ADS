#EXERCICIO 3: LER DOIS NUMERO E EXIBIR A SOMA, SUBTRAÇÃO, MULTIPLICAÇÃO E DIVISÃO

entrada = input("Digite dois valor: ")
numeros = list(map(float, entrada.split()))

if numeros[1] == 0:
    validacaoDivisao = "Erro: Não é possível dividir por zero"
else:
    validacaoDivisao = f"A divisão é {numeros[0] / numeros[1]}"

print(f"A soma é {numeros[0] + numeros[1]}")
print(f"A subtração é {numeros[0] - numeros[1]}")
print(f"A multiplicação é {numeros[0] * numeros[1]}")
print(f"{validacaoDivisao}")
