#LER DOIS NUMEROS E EXIBIR O QUOCIENTE E O RESTRO DA DIVISÃO ENTRE ELES
entrada = input("Digite dois numeros: ")
numeros = list(map(int, entrada.split()))
print(f"Quociente: {numeros[0] / numeros[1]}\nResto da divisão: {numeros[0] % numeros[1]}")