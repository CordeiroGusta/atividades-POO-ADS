# CRIE UMA FUNÇÃO QUE RETORNA TRUE SE O NUMERO FOR PRIMO E FALSE SE NAO FOR
def eh_primo(numero: int):
    if numero <= 1:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False
            
    return True

numero = int(input("Digite um número: "))
print(f"O seu número é primo: {eh_primo(numero)}")