
# Iteráveis e Iteradores

O `for` permite percorrer uma sequência ou coleção de elementos e executar um bloco de código para cada elemento.

Por exemplo:

```python
nomes = ["Eduardo", "Antonio", "Carlos"]

for nome in nomes:
    print(nome)
```

Por trás do `for`, Python utiliza um mecanismo chamado **iteração**.

Para entender esse mecanismo, precisamos diferenciar dois conceitos:

* **iterável** → objeto que pode fornecer um iterador;
* **iterador** → objeto que fornece os elementos, um por vez.

---

## Iterável

Um **iterável** (*iterable*) é um objeto que pode ser percorrido.

Alguns exemplos:

* listas (`list`);
* tuplas (`tuple`);
* strings (`str`);
* dicionários (`dict`);
* conjuntos (`set`);
* objetos `range`.

Um objeto iterável fornece o método especial `__iter__()`, que retorna um **iterador**.

Podemos pensar assim:

```text
iterável
   │
   │ __iter__()
   ▼
iterador
```

Por exemplo:

```python
texto = "Python"

iterador = iter(texto)
```

A função `iter()` solicita ao objeto um iterador.

---

## Iterador

Um **iterador** (*iterator*) é um objeto responsável por fornecer os elementos de um iterável, **um por vez**.

Ele implementa o método especial `__next__()`.

Podemos solicitar o próximo elemento utilizando a função `next()`:

```python
texto = "Python"

iterador = iter(texto)

print(next(iterador))
print(next(iterador))
print(next(iterador))
```

Resultado:

```text
P
y
t
```

Cada chamada de `next()` avança o estado do iterador.

---

## `iter()`

A função `iter()` recebe um objeto iterável e retorna um iterador.

```python
palavra = "Python"

iterador = iter(palavra)
```

Podemos verificar os objetos:

```python
print(palavra)
print(iterador)
```

Conceitualmente:

```text
"Python"
   │
   │ iter()
   ▼
iterador
```

O objeto `"Python"` é o **iterável**.

O objeto retornado por `iter()` é o **iterador**.

---

## `next()`

A função `next()` solicita ao iterador o próximo elemento.

```python
palavra = "Python"

iterador = iter(palavra)

print(next(iterador))  # P
print(next(iterador))  # y
print(next(iterador))  # t
print(next(iterador))  # h
print(next(iterador))  # o
print(next(iterador))  # n
```

Depois que todos os elementos forem consumidos, não existe mais um próximo elemento.

```python
print(next(iterador))
```

Nesse momento, o iterador levanta a exceção:

```text
StopIteration
```

---

## Iteradores possuem estado

Uma característica importante de um iterador é que ele **mantém o estado da iteração**.

Considere:

```python
texto = "Python"

iterador = iter(texto)
```

Inicialmente, nenhum caractere foi consumido.

Depois:

```python
next(iterador)
```

o iterador entrega:

```text
P
```

Agora seu estado avançou.

Outra chamada:

```python
next(iterador)
```

entrega:

```text
y
```

E assim por diante:

```text
iterador
   │
   ▼
P → y → t → h → o → n → StopIteration
```

---

## `for` por baixo dos panos

Agora podemos entender melhor o que acontece quando utilizamos:

```python
for letra in "Python":
    print(letra)
```

Conceitualmente, o Python faz algo semelhante a:

```python
iterador = iter("Python")

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break
```

Ou seja, o `for` utiliza o **protocolo de iteração** para obter os elementos um por vez.

---

## Protocolo de iteração

Para que um objeto seja um iterador, ele precisa implementar:

```python
__iter__()
__next__()
```

O método `__iter__()` de um iterador normalmente retorna o próprio iterador.

O método `__next__()` retorna o próximo elemento ou levanta `StopIteration` quando não existem mais elementos.

Podemos representar o protocolo desta forma:

```text
              iterável
                 │
                 │ __iter__()
                 ▼
              iterador
                 │
                 │ __next__()
                 ▼
             próximo valor
                 │
                 ├── ainda existem valores
                 │         │
                 │         └──► próximo valor
                 │
                 └── não existem mais
                           │
                           ▼
                    StopIteration
```

---

## Exemplo sem `for`

Podemos implementar manualmente a iteração:

```python
texto = "Antonio"

iterador = iter(texto)

while True:
    try:
        letra = next(iterador)
        print(letra)

    except StopIteration:
        break
```

Resultado:

```text
A
n
t
o
n
i
o
```

O `for` faz esse trabalho automaticamente, por isso normalmente não precisamos escrever esse código manualmente.

---

## Iterável ≠ Iterador

É importante não confundir os dois conceitos.

```python
texto = "Python"

iterador = iter(texto)
```

Aqui:

```text
texto     → iterável
iterador  → iterador
```

O iterável é o objeto que pode fornecer um iterador.

O iterador é o objeto que controla o estado da iteração e fornece os valores individualmente.

Uma analogia útil é:

> O iterável é a estante com os livros. 📚
> O iterador é a pessoa que percorre a estante entregando um livro por vez.

---

### Um detalhe que vale muito a pena guardar

**`for` não é simplesmente "um contador automático".**

Ele não precisa saber o tamanho da estrutura nem acessar seus elementos por índice.

Por isso isto funciona:

```python
for letra in "Python":
    print(letra)
```

e isto também:

```python
for numero in {10, 20, 30}:
    print(numero)
```

e também:

```python
for linha in arquivo:
    print(linha)
```

O mecanismo comum entre eles é o **protocolo de iteração**. Isso é uma das partes fundamentais do modelo de objetos do Python.
