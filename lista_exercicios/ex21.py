#CONTAR E EXIBIR TODOS OS NUMEROS PARES ENTRE 1 E 50
contador = 0
for i in range (1, 51):
    if i % 2 == 0:
        print(i)
        contador = contador + 1
        print(f"{contador} números\n")