#LER A BASE E ALTURA E RETORNAR A SUA AREA E PERIMETRO

entrada = input("Digite a base e a altura de um retângulo: ")
medida = list(map(float, entrada.split()))

area = medida[0] * medida[1]
perimetro = (2 * medida[0]) + (2 * medida[1])

print(f"A Área do retângulo é: {area}\nE o perímetro: {perimetro}")