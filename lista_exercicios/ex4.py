#EXERCICIO 4: LER DOIS VALORES E INVERTER OS MESMOS

a = float(input("Digite o valor A: "))
b = float(input("Digite o valor B: "))

a, b = b, a

print(f"Valor A: {a}\nValor B: {b}")