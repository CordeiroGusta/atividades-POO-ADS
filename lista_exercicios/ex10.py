# LER UM VALOR E DIZER QUE TIPO DE DADO É VALOR
from ex10_type import tipoDado

entrada = input("Digite um valor: ")
entrada = tipoDado(entrada)
print(f"A entrada é do tipo: {type(entrada)}")