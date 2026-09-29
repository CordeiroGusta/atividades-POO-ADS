#exercicio 01

a, b = list(map(float, input("Digite dois numeros: ").split()))

if b != 0:
    validacaoDivisao = f"A divisão é: {a / b}"
else:
    validacaoDivisao = "Não é possível dividir por zero"

print(f"A soma é: {a + b}\nA subtração: {a - b}\nA multiplicação é: {a * b}\n{validacaoDivisao}")