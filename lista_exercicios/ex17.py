#LER AS MEDIDAS DE TRÊS LADOS DO TRIÂNGULO E DIZER SE ELE É EQUILATERO, ISOSCELES OU ESCALENO
entrada = input("Digite os três lados do triângulo: ")
lados = list(map(float, entrada.split()))

if lados[0] == lados[1] == lados[2]:
    print("É um triângulo Equilátero")
elif lados[0] == lados[1] or lados[0] == lados[2]:
    print("É um triângulo Isósceles")
else:
    print("É um triângulo Escaleno")