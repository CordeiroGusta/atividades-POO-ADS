#Ler uma idade e dizer se é criança, adolescente, adulto, ou idoso
idade = int(input("Digite a sua idade: "))

if idade <= 12:
    print("Criança")
elif idade >= 12 and idade <= 18:
    print("Adolescente")
elif idade >= 18 and idade <= 59:
    print("Adulto")
else:
    print("Idoso")