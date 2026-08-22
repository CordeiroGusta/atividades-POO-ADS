# FUNÇÃO QUE RECEBE UM PARÂMETRO PADRÃO 
def calcular_desconto(preco, percentual=10):
    desconto = preco * percentual/100
    return preco - desconto

preco = float(input("Digite um valor: "))
percentual = input("Digite um percentual, se desejar (caso não seja fornecido, um percentual de 10% sera usado): ")

if percentual == "" or percentual is None:
    print(f"O valor com o desconto será de: {calcular_desconto(preco)}")
else:
    print(f"O valor com o desconto será de: {calcular_desconto(preco, float(percentual))}")