#LER 5 NOMES E EXIBIR ELES EM ORDEM ALFABÉTICA
entrada = input("Digite 5 nomes: ")
nomes = list(map(str, entrada.split()))
nomes.sort()

print("Os nomes em ordem alfabética é:")
for i in nomes:
    print(i)