'''
1. Conta bancária
Um banco precisa garantir que seus clientes não alterem diretamente o saldo. Crie a classe ContaBancaria com __titular e __saldo.
 - Inicialize os atributos no construtor e rejeite saldo inicial negativo.
 - Implemente depositar(valor) e sacar(valor).
 - Impeça depósitos não positivos e saques maiores que o saldo.
 - Crie uma propriedade somente leitura para consultar o saldo.
 - Teste depósitos, saques e operações inválidas.
'''

class ContaBancaria:
    def __init__(self, titular: str, saldo_inicial: float=0) -> None: #retornando None pq o init não cria algo novo, ele inicia o objeto criado com __new__
        if saldo_inicial < 0:
            raise ValueError("Saldo inicial inválido")
        self.__titular = titular
        self.__saldo = saldo_inicial

    @property
    def saldo(self) -> float: # float pq eu estou retornando o valor do saldo que foi tipado como float
        return self.__saldo

    @property
    def titular(self) -> str: # str pq eu estou retornando o nome do titular que foi tipado como uma str
        return self.__titular

    def depositar(self, valor) -> None:
        if valor <= 0:
            raise ValueError("O valor a ser depositado deve ser maior que zero!")
        
        self.__saldo += valor

    def sacar(self, valor) -> None: # tanto depositar quanto sacar devem retornar None pq eles apenas mutam, ou seja, alteram algo ja existente, e não retornam algo especifico com return
        if valor <= 0:
            raise ValueError("Valor de saque deve ser maior que zero!")
        if self.__saldo < valor:
            raise ValueError("Saldo insuficiente!")

        self.__saldo -= valor

nome = str(input("Digite o nome do titular: "))
saldo_inicial = float(input("Digite o saldo inicial da conta: "))
pessoa1 = ContaBancaria(nome, saldo_inicial)

print(f"Nome: {pessoa1.titular}\nSaldo: {pessoa1.saldo}")
print("\nTestando os metódos de Deposito e Saque!")
valor_deposito = float(input("DEPOSITO\nDigite um valor de deposito válido: "))
try:
    pessoa1.depositar(valor_deposito)
except ValueError as e: #Pega o ValueError levantado durante a validação
    print(f"Erro durante o processo de deposito: {e}")
else: # bloco else em um except, executa um bloco caso não tenha nenhuma excessão
    print(f"Deposito de {valor_deposito} realizado com sucesso!\nSaldo atual na conta de {pessoa1.titular}: {pessoa1.saldo}")

print("\nSAQUE!")
valor_saque = float(input(f"Saldo atual: {pessoa1.saldo}\nDigite um valor de saque válido: "))
try:
    pessoa1.sacar(valor_saque)
except ValueError as e:
    print(f"Erro durante o processo de saque: {e}")
else:
    print(f"Saque de {valor_saque} realizado na conta de {pessoa1.titular}\nSaldo atual na conta de {pessoa1.titular}: {pessoa1.saldo}")