#LER UM NUMERO E EXIBIR A TABUADA DELE DO 1 AO 10
numero = float(input("Digite um número: "))

for i in range(1,11):
    print(f"{i} x {numero} = {i * numero}")