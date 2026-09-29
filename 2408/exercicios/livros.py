class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def ficha(self):
        return f"Título: {self.titulo} ---Autor: {self.autor}"

livro1 = Livro("O Inferno de Dante", "Dante Alighierri")
print(f"A ficha do livro é: {livro1.ficha()}")