# 🐍 Revisão de Fundamentos Python — Exercícios 1 a 40

Este diretório reúne uma sequência de **40 exercícios práticos** desenvolvidos durante uma revisão dos fundamentos de Python.

Mais do que completar exercícios, esta etapa serviu para transformar conceitos isolados em ferramentas que consigo raciocinar e aplicar.

---

## 🎯 O que esta lista representa

A progressão dos exercícios percorre desde operações e entradas simples até conceitos que exigem uma compreensão maior do funcionamento da linguagem:

```text
Entrada de dados
      ↓
Conversão e tratamento de tipos
      ↓
Operações e lógica condicional
      ↓
Laços de repetição
      ↓
Listas e manipulação de dados
      ↓
Strings
      ↓
Funções e parâmetros
      ↓
Parâmetros padrão
      ↓
Unpacking / Desempacotamento
      ↓
*args
      ↓
Recursividade
```

O objetivo principal foi construir uma base que permita olhar para um problema e entender **como decompor o problema em partes menores**, quais dados entram, como são transformados e como o resultado é produzido.

---

# 🧠 Principais conhecimentos consolidados

## 1. Entrada e tratamento de dados

Os primeiros exercícios trabalham diretamente com `input()` e mostram uma característica fundamental do Python:

```python
entrada = input("Digite um valor: ")
```

O valor recebido por `input()` é uma `str`, independentemente do que o usuário tenha digitado.

A partir disso, foram praticadas conversões como:

```python
int(entrada)
float(entrada)
```

Também foi explorada uma abordagem mais robusta para tentar identificar o tipo do dado recebido, utilizando `try/except`.

Isso ajudou a consolidar uma ideia importante:

> **Entrada de dados não significa apenas receber informação; é necessário interpretar e transformar essa informação para que o programa consiga trabalhar com ela.**

---

## 2. Manipulação de listas

Ao longo dos exercícios, listas passaram a ser utilizadas para armazenar e manipular conjuntos de dados:

```python
numeros = list(map(float, entrada.split()))
```

Foram praticados conceitos como:

- criação de listas;
- `append()`;
- acesso por índice;
- iteração;
- `max()` e `min()`;
- `sum()`;
- `sort()`;
- remoção de duplicados;
- construção de listas por compreensão;
- passagem de listas para funções.

Um dos pontos importantes foi perceber que uma lista não é apenas uma "caixa de vários valores": ela pode ser processada, transformada, percorrida e utilizada como estrutura de dados dentro de outras operações.

---

## 3. Manipulação de strings

Os exercícios também exploraram strings como estruturas que podem ser processadas caractere por caractere.

Entre os conceitos praticados:

- `split()`;
- `join()`;
- `lower()`;
- acesso a caracteres;
- inversão de strings;
- identificação de vogais;
- tratamento de nomes;
- verificação de palíndromos;
- compreensão de strings como sequências iteráveis.

Exemplo:

```python
palavra_inversa = "".join(palavra)
```

Essa etapa ajudou a consolidar a ideia de que strings também podem ser percorridas e transformadas por meio das ferramentas da linguagem.

---

# 🔧 Funções

A partir dos exercícios 33 em diante, o foco passa a ser cada vez mais a criação de funções.

Exemplo:

```python
def soma(a, b):
    return a + b
```

Foi praticada a diferença entre:

- receber informações;
- processar informações;
- retornar informações.

Isso muda a forma de pensar o código.

Em vez de concentrar toda a lógica no programa principal, uma responsabilidade pode ser encapsulada em uma função e reutilizada.

---

# ⚙️ Parâmetros padrão — Exercício 37

No exercício 37 foi trabalhado um conceito especialmente importante:

```python
def calcular_desconto(preco, percentual=10):
```

Nesse caso, `percentual` possui um **valor padrão**.

Isso significa que:

```python
calcular_desconto(100)
```

utiliza automaticamente:

```text
percentual = 10
```

Enquanto:

```python
calcular_desconto(100, 20)
```

substitui o valor padrão.

Mais importante do que decorar a sintaxe foi compreender o comportamento:

> **O parâmetro padrão é utilizado quando nenhum argumento correspondente é fornecido na chamada da função.**

Esse conceito será extremamente útil posteriormente em APIs, métodos de classes e construção de funções mais flexíveis.

---

# 📦 Unpacking / Desempacotamento — Exercício 38

O exercício 38 foi um dos pontos em que a compreensão dos parâmetros de funções avançou significativamente.

Foi utilizada a estrutura:

```python
def soma(*numeros):
    return sum(numeros)
```

E a chamada:

```python
soma(*numeros)
```

Isso levou ao estudo do **unpacking**, ou desempacotamento.

Por exemplo:

```python
valores = [10, 20, 30]

soma(*valores)
```

é conceitualmente equivalente a:

```python
soma(10, 20, 30)
```

O `*` nesse contexto pega os elementos de uma estrutura iterável e os distribui como argumentos posicionais.

A partir desse conceito, foram estudados também:

```python
*args
```

e:

```python
**kwargs
```

### `*args`

Permite que uma função receba uma quantidade variável de argumentos posicionais.

```python
def soma(*numeros):
    ...
```

Dentro da função, `numeros` será uma **tupla** contendo os argumentos recebidos.

### `**kwargs`

Segue a mesma ideia para argumentos nomeados:

```python
def exemplo(**dados):
    ...
```

Nesse caso, os argumentos são recebidos como um **dicionário**.

Essa descoberta foi importante porque mostrou que a sintaxe do Python não é apenas uma forma de escrever código: ela representa comportamentos específicos na forma como os argumentos são empacotados e desempacotados.

---

# ♻️ Recursividade — Exercício 40

O exercício 40 foi um dos maiores pontos de aprendizado desta lista.

Foi implementada uma função recursiva para calcular a sequência de Fibonacci para uma posição informada:

```python
def fibonacci(posicao):
    if posicao == 0:
        return 0

    if posicao == 1:
        return 1

    return fibonacci(posicao - 2) + fibonacci(posicao - 1)
```

A sequência segue a definição:

```text
F(0) = 0
F(1) = 1

F(n) = F(n - 1) + F(n - 2)
```

Para:

```python
fibonacci(10)
```

a função chega a:

```text
F(10)
= F(8) + F(9)
= 21 + 34
= 55
```

O mais importante neste exercício não foi apenas obter `55`.

Foi compreender o mecanismo da recursividade:

1. uma chamada da função gera novas chamadas;
2. cada chamada fica aguardando os resultados necessários;
3. as chamadas continuam até atingir um caso-base;
4. os valores começam então a retornar;
5. cada chamada utiliza os resultados recebidos para concluir seu próprio cálculo.

Visualmente, uma chamada como:

```text
fibonacci(5)
```

pode ser entendida como uma árvore:

```text
                 F(5)
               /     \
             F(3)    F(4)
            /   \    /   \
          F(1) F(2) F(2) F(3)
               / \  / \  / \
             F(0) F(1) ...
```

Essa experiência consolidou não apenas a sintaxe de uma função recursiva, mas também a relação entre **definição matemática, decomposição de problemas e fluxo de execução**.

---

# 📚 Exercícios por conceito

| Exercícios | Principais conceitos |
|---|---|
| 01–10 | Entrada, conversão e tratamento de dados |
| 11–18 | Funções, operações e condicionais |
| 19–24 | Laços, contadores, listas e Fibonacci iterativo |
| 25–32 | Strings, listas e manipulação de coleções |
| 33–36 | Funções, parâmetros e retorno |
| 37 | Parâmetro padrão |
| 38 | Unpacking e `*args` |
| 39 | Função recebendo uma lista |
| 40 | Recursividade e Fibonacci |

---

# 🔎 O que esta etapa consolidou

Ao finalizar os exercícios, os principais fundamentos trabalhados foram:

### Dados

- `input()`;
- conversão de tipos;
- `int`;
- `float`;
- `str`;
- tratamento de exceções;
- validação de entradas.

### Estruturas de dados

- listas;
- tuplas;
- strings;
- iteração;
- compreensão de listas;
- manipulação de coleções.

### Controle de fluxo

- `if`;
- `elif`;
- `else`;
- `for`;
- `while`;
- `break`.

### Funções

- definição;
- parâmetros;
- argumentos;
- `return`;
- parâmetros padrão;
- múltiplos argumentos;
- `*args`;
- `**kwargs`;
- unpacking.

### Raciocínio

- decomposição de problemas;
- identificação de casos-base;
- transformação de dados;
- reutilização de lógica;
- análise do fluxo de execução;
- raciocínio recursivo.

---





# 📌 Observação sobre o projeto

Este repositório não representa apenas uma coleção de respostas para exercícios.

Ele representa uma etapa de construção de base.

Algumas soluções podem ser simplificadas, otimizadas ou escritas de maneiras diferentes. Isso é intencional dentro do contexto de aprendizado: o foco desta etapa foi principalmente **entender os fundamentos, testar hipóteses, observar o comportamento do código e desenvolver raciocínio de programação.**

O código é, portanto, também um registro da evolução do processo de aprendizagem.

#



## 🛠️ Tecnologias

- Python 3
- VS Code
- Git / GitHub


