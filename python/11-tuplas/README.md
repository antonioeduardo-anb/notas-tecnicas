
# Tuplas (`tuple`)

As tuplas são estruturas de dados utilizadas para armazenar múltiplos valores em um único objeto.

Elas se parecem bastante com as listas, mas possuem uma diferença fundamental: as tuplas são **imutáveis**.

Isso significa que, depois de serem criadas, os seus elementos não podem ser alterados.

---

## Características

As tuplas:

* mantêm a ordem dos elementos;
* permitem valores repetidos;
* aceitam diferentes tipos de dados;
* podem ser percorridas com `for`;
* permitem acesso por índices;
* são imutáveis.

---

## Criando tuplas

Uma tupla pode ser criada utilizando parênteses.

```python
nomes = ("Eduardo", "Carlos", "João")
```

Também é possível omitir os parênteses.

```python
cores = "azul", "verde", "amarelo"
```

O Python produzirá o mesmo resultado.

---

## Representação

```text
nomes
   │
   ▼
┌──────────┬──────────┬────────┐
│ Eduardo  │ Carlos   │ João   │
├──────────┼──────────┼────────┤
│    0     │    1     │    2   │
└──────────┴──────────┴────────┘
```

---

# Índices

Assim como as listas, as tuplas utilizam índices.

```python
nomes = ("Eduardo", "Carlos", "João")

print(nomes[0])
print(nomes[1])
print(nomes[2])
```

Resultado:

```text
Eduardo
Carlos
João
```

---

## Índices negativos

Também é possível acessar os elementos de trás para a frente.

```python
nomes = ("Eduardo", "Carlos", "João")

print(nomes[-1])
```

Resultado:

```text
João
```

---

# Imutabilidade

Uma tupla não pode ser modificada.

Por exemplo:

```python
nomes = ("Eduardo", "Carlos", "João")

nomes[0] = "Pedro"
```

Isso produzirá um erro.

```text
TypeError: 'tuple' object does not support item assignment
```

---

## Métodos ausentes

As tuplas não possuem métodos utilizados para modificar listas, como:

```python
append()
remove()
insert()
pop()
```

---

# O caso especial das tuplas com um único elemento

Em Python, a vírgula é o elemento que define uma tupla, e não os parênteses.

---

### Correto

```python
tupla = ("valor",)
```

ou

```python
tupla = "valor",
```

---

### Incorreto

```python
texto = ("valor")
```

Nesse caso, o Python interpreta a expressão apenas como uma *string* cercada por parênteses.

---

### Verificando os tipos

```python
tupla = ("valor",)

texto = ("valor")

print(type(tupla))
print(type(texto))
```

Resultado:

```text
<class 'tuple'>
<class 'str'>
```

---

# Conversão de tipos (*casting*)

Também é possível converter listas em tuplas.

```python
lista_frutas = ["Maçã", "Pera"]

tupla_frutas = tuple(lista_frutas)
```

Resultado:

```text
('Maçã', 'Pera')
```

Da mesma forma, podemos converter uma tupla em uma lista.

```python
nomes = ("Eduardo", "Carlos")

lista_nomes = list(nomes)
```

---

# Percorrendo uma tupla

```python
nomes = ("Eduardo", "Carlos", "João")

for nome in nomes:
    print(nome)
```

Resultado:

```text
Eduardo
Carlos
João
```

---

# Desempacotamento

As tuplas também podem ser desempacotadas.

```python
coordenadas = (10, 20)

x, y = coordenadas
```

Resultado:

```text
x = 10

y = 20
```

---

# Por que utilizar tuplas?

### Segurança

A imutabilidade reduz a possibilidade de alterações acidentais.

---

### Desempenho

Como a estrutura não pode ser alterada, algumas operações são executadas de forma mais eficiente.

---

### Utilização como chave

As tuplas podem ser utilizadas como chaves em dicionários.

```python
coordenadas = {
    (10, 20): "Casa"
}
```

Isso não seria possível com listas.

```python
coordenadas = {
    [10, 20]: "Casa"
}
```

Resultado:

```text
TypeError: unhashable type: 'list'
```

Em Python, muitos valores retornados por funções são tuplas, justamente porque elas oferecem mais segurança e previsibilidade. 🚀
