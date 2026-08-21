#EXIBIR OS DEZ PRIMEIROS TERMOS DA SEQUENCIA DE FIBONNACI
numero_atual = 0
proximo_numero = 1

fibonnaci = []

for i in range(0,11):
    fibonnaci.append(numero_atual)
    numero_atual, proximo_numero = proximo_numero, numero_atual + proximo_numero

for j in fibonnaci:
    print(j)