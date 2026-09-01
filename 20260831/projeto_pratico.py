class ContaBancaria:
    def __init__(self, titular, cpf, numero_conta, agencia, saldo):
        self.titular = titular
        self.cpf = cpf
        self.numero_conta = numero_conta
        self.agencia = agencia
        self.saldo = saldo

    def depositar(self, valor):
        if valor <= 0:
            return "Digite um valor maior que zero"
        
        self.saldo = self.saldo + valor
        return self.saldo

    def sacar(self, valor):
        if self.saldo < valor:
            return "Saldo insuficiente"

        self.saldo = self.saldo - valor
        return self.saldo

    def mostrar_saldo(self):
        return self.saldo

    def efetuar_transacao(self, valor, chave_destinatario):
        if self.saldo < valor:
            return "Saldo insuficiente"

        self.saldo = self.saldo - valor
        return f'transferencia realizada de {valor} para a conta {chave_destinatario}\nSaldo atual: {self.mostrar_saldo()}'


fulano = ContaBancaria('Fulano', 32165498701, 7223, 2, 2500)

print("\nDados da Conta")
print(f"Titular: {fulano.titular}")
print(f"CPF: {fulano.cpf}")
print(f"Numero de Conta: {fulano.numero_conta}")
print(f"Agência: {fulano.agencia}")
print(f"Saldo: {fulano.saldo}")

print("\nMetodos:")
print(f"Deposito de 500 na conta: {fulano.depositar(500)}")
print(f"Saque de 200: {fulano.sacar(200)}")
print(f"Mostrar o saldo da conta: {fulano.mostrar_saldo()}")
print(f"Transação para uma conta: {fulano.efetuar_transacao(300, 78945612387)}")