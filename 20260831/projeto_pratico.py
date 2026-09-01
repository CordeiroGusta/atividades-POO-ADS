class ContaBancaria:
    # def __init__(self, titular, cpf, numero_conta, agencia, saldo, extrato):
    def __init__(self, titular, cpf, numero_conta, agencia, saldo):
        self.titular = titular,
        self.cpf = cpf,
        self.numero_conta = numero_conta,
        self.agencia = agencia,
        self.saldo = saldo
        # self.extrato = extrato

    def depositar(self, valor):
        self.saldo = self.saldo + valor
        return self.saldo

    # def saque(self, valor):
    #     self.saldo

teste = ContaBancaria('Portes', 32156498701, 100000115, 3, 150)
print(teste.saldo)
print(f"Com mais 10, o saldo fica: {teste.depositar(50)}")