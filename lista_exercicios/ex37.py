# FUNÇÃO QUE RECEBE UM PARÂMETRO PADRÃO 
def desconto(preco, percentual=10):
    if percentual == "":
        desconto = preco * (percentual/100)
        valor_final = preco - desconto
    else: 
        
    return valor_final

preco = float(input("Digite um preço: "))
percentual = float(input("Digite um desconto, se quiser: "))
print(f"Desconto do valor: {desconto(preco, percentual)}")