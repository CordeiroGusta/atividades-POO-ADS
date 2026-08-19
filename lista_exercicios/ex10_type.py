# LER UM VALOR E DIZER QUE TIPO DE DADO É VALOR
def tipoDado (dado: str):
    '''Input sempre retorna str, por isso, esse função analisa com precisão a entrada do usuário'''
    #Tenta Inteiro
    try:
        return(int(dado))
    except ValueError:
        pass

    #Tenta float
    try:
        return(float(dado))
    except ValueError:
        pass

    #Tenta Bool (True ou False)
    dado.lower()
    if dado == 'true':
        return True
    if dado == 'false':
        return False

    return dado