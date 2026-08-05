
# Desempacotamento (*unpacking*)

O desempacotamento (*unpacking*) é uma técnica utilizada para extrair elementos de um objeto iterável e armazená-los diretamente em variáveis.

Entre os objetos que podem ser desempacotados estão:

* listas (`list`);
* tuplas (`tuple`);
* strings (`str`);
* conjuntos (`set`);
* dicionários (`dict`).

---

## Sintaxe

```python
variavel_1, variavel_2 = iteravel
```

O Python percorre o iterável e distribui os valores entre as variáveis.

---

## Exemplo básico

```python
nomes = ["Antonio", "Carlos", "Miguel"]

n1, n2, n3 = nomes

print(n1)
print(n2)
print(n3)
```

Saída:

```text
Antonio
Carlos
Miguel
```

---

## O que acontece internamente?

Imagine a seguinte lista:

```python
nomes = ["Antonio", "Carlos", "Miguel"]
```

O Python executa algo semelhante a isto:

```text
n1 = "Antonio"
n2 = "Carlos"
n3 = "Miguel"
```

Podemos representar o processo desta maneira:

```text
["Antonio", "Carlos", "Miguel"]
       │         │          │
       ▼         ▼          ▼
      n1        n2         n3
```

---

## Quantidade de elementos

O número de variáveis deve corresponder ao número de elementos.

Por exemplo:

```python
nomes = ["Antonio", "Carlos", "Miguel"]

n1, n2, n3 = nomes
```

Isso funciona corretamente.

Entretanto:

```python
n1, n2 = nomes
```

produzirá um erro.

```text
ValueError: too many values to unpack
```

Isso acontece porque existem três elementos, mas apenas duas variáveis.

---

## Utilizando `*`

O operador `*` permite agrupar vários elementos em uma única variável.

```python
primeiro, *resto = ["Davi", "Rita", "Leandro", "José"]
```

Resultado:

```text
primeiro = "Davi"

resto = ["Rita", "Leandro", "José"]
```

Representação:

```text
["Davi", "Rita", "Leandro", "José"]
    │         └───────────────┐
    ▼                         ▼
primeiro                   resto
```

---

## O operador `*` no meio da sequência

O operador também pode ser utilizado no centro da atribuição.

```python
primeiro, *meio, ultimo = [1, 2, 3, 4, 5]
```

Resultado:

```text
primeiro = 1

meio = [2, 3, 4]

ultimo = 5
```

---

## Ignorando valores

Existe uma convenção muito utilizada em Python para indicar que determinado valor será ignorado.

```python
n1, _, n3 = ["Ana", "Beatriz", "Caio"]
```

Resultado:

```text
n1 = "Ana"

n3 = "Caio"
```

---

## Utilizando `_` e `*` simultaneamente

```python
n1, _, n3, *_ = [
    "Ana",
    "Beatriz",
    "Caio",
    "Duda",
    "Elaine"
]
```

Resultado:

```text
n1 = "Ana"

n3 = "Caio"
```

---

## Desempacotando strings

Como uma string é uma sequência de caracteres, ela também pode ser desempacotada.

```python
texto = "Python"

a, b, c, d, e, f = texto
```

Resultado:

```text
a = "P"
b = "y"
c = "t"
d = "h"
e = "o"
f = "n"
```

---

## Desempacotando listas aninhadas

```python
dados = ["Antonio", [10, 20]]

nome, numeros = dados
```

Resultado:

```text
nome = "Antonio"

numeros = [10, 20]
```

Também podemos fazer isto:

```python
nome, [n1, n2] = ["Antonio", [10, 20]]
```

Resultado:

```text
nome = "Antonio"

n1 = 10

n2 = 20
```
