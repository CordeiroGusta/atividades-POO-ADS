# REMOVER ELEMENTOS DUPLICADOS DE UMA LISTA
entrada = input("Digite alguns valores: ")
numeros = list(map(float, entrada.split()))

sem_duplicados = []

for i in numeros:
    if i not in sem_duplicados:
        sem_duplicados.append(i)

print(f"Lista digitada: {numeros}")
print(f"Lista sem os duplicados: {sem_duplicados}")