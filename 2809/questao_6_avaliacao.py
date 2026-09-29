class Pessoa:
    def __init__(self, nome, altura, peso):
        self.nome = nome
        self.altura = altura
        self.peso = peso

    def mostrar_dados(self):
        return f"Nome: {self.nome}\nAltura: {self.altura}\nPeso: {self.peso}"

    def calcular_imc(self):
        if self.altura <= 0:
            return("Altura invalida!")
        else:
            imc = float(self.peso/(self.altura ** 2))
            return imc

    def classificar_imc(self):
        imc = self.calcular_imc()
        if imc < 18.5:
            return f"{self.calcular_imc():.2f} é considerado abaixo do peso!"
        elif imc >= 18.5 and imc <= 24.9:
            return f"{self.calcular_imc():.2f} é considerado peso normal!"
        elif imc >= 25.0 and imc <= 29.9:
            return f"{self.calcular_imc():.2f} é considerado sobrepeso!"
        else:
            return f"{self.calcular_imc():.2f} é considerado obesidade!"

nome = input("Digite o seu nome: ")
altura = float(input("Digite sua altura(em metros): "))
peso = float(input("Digite seu peso: "))

pessoa1 = Pessoa(nome, altura, peso)
print(f"\n{pessoa1.mostrar_dados()}")
print(f"\nIMC: {pessoa1.calcular_imc():.2f}")

print(pessoa1.classificar_imc())