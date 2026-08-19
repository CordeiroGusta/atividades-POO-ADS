# CONVERTER DE CELSIUS PARA FAHRENHEIT
def Fahrenheit(temperatura):
    return (temperatura * 1.8) + 32

celsius = float(input("Digite uma temperatura: "))

print(f"Temperatura em Celsius: {celsius}\nTemperatura em Fahrenheit: {Fahrenheit(celsius)}")