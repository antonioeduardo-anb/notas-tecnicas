
# Listas (`list`)

As listas são estruturas de dados utilizadas para armazenar múltiplos valores em uma única variável.

Em Python, as listas possuem as seguintes características:

* mantêm a ordem dos elementos;
* permitem a modificação dos valores (*mutabilidade*);
* podem armazenar diferentes tipos de dados;
* permitem a existência de elementos repetidos;
* utilizam índices para acessar os elementos.

---

## Criando uma lista

As listas são delimitadas por colchetes (`[]`).

```python
frutas = ["Maçã", "Banana", "Uva"]
```

Podemos representar essa estrutura da seguinte maneira:

```text
frutas
   │
   ▼
┌───────────┬───────────┬───────────┐
│ "Maçã"    │ "Banana"  │ "Uva"     │
├───────────┼───────────┼───────────┤
│     0     │     1     │     2     │
└───────────┴───────────┴───────────┘
```

---

## Índices

Cada elemento possui uma posição numérica chamada **índice**.

O primeiro elemento está na posição `0`.

```python
frutas = ["Maçã", "Banana", "Uva"]
```

| Índice | Valor      |
| ------ | ---------- |
| `0`    | `"Maçã"`   |
| `1`    | `"Banana"` |
| `2`    | `"Uva"`    |

---

## Acessando elementos

```python
frutas = ["Maçã", "Banana", "Uva"]

print(frutas[0])
print(frutas[1])
print(frutas[2])
```

Saída:

```text
Maçã
Banana
Uva
```

---

## Índices negativos

Também é possível percorrer a lista na direção oposta.

```python
frutas = ["Maçã", "Banana", "Uva"]
```

| Índice | Valor      |
| ------ | ---------- |
| `-1`   | `"Uva"`    |
| `-2`   | `"Banana"` |
| `-3`   | `"Maçã"`   |

Exemplo:

```python
print(frutas[-1])
```

Saída:

```text
Uva
```

---

## Mutabilidade

As listas são objetos mutáveis.

Isso significa que seus elementos podem ser alterados após a criação da lista.

```python
frutas = ["Maçã", "Banana", "Uva"]

frutas[1] = "Morango"

print(frutas)
```

Saída:

```text
['Maçã', 'Morango', 'Uva']
```

---

## O que acontece internamente?

Antes da alteração:

```text
frutas
   │
   ▼
["Maçã", "Banana", "Uva"]
```

Depois da alteração:

```text
frutas
   │
   ▼
["Maçã", "Morango", "Uva"]
```

---

## Adicionando elementos

### `append()`

Adiciona um elemento ao final da lista.

```python
frutas = ["Maçã", "Banana"]

frutas.append("Uva")
```

Resultado:

```text
['Maçã', 'Banana', 'Uva']
```

---

### `insert()`

Insere um elemento em uma posição específica.

```python
frutas.insert(1, "Morango")
```

Resultado:

```text
['Maçã', 'Morango', 'Banana', 'Uva']
```

---

## Removendo elementos

### `remove()`

Remove um elemento pelo valor.

```python
frutas.remove("Banana")
```

---

### `pop()`

Remove um elemento pelo índice.

```python
frutas.pop(1)
```

---

## Percorrendo listas

Podemos utilizar um laço `for`.

```python
frutas = ["Maçã", "Banana", "Uva"]

for fruta in frutas:
    print(fruta)
```

Saída:

```text
Maçã
Banana
Uva
```

---

## Matrizes

Uma matriz pode ser representada por uma lista contendo outras listas.

```python
matriz = [
    [1, 2],
    [3, 4],
    [5, 6]
]
```

Podemos visualizar a estrutura da seguinte maneira:

```text
┌─────┬─────┐
│  1  │  2  │
├─────┼─────┤
│  3  │  4  │
├─────┼─────┤
│  5  │  6  │
└─────┴─────┘
```

---

## Acessando os elementos

A sintaxe utilizada é:

```python
lista[linha][coluna]
```

---

### Acessando o número `2`

```python
print(matriz[0][1])
```

```text
linha 0 → [1, 2]
coluna 1 → 2
```

Resultado:

```text
2
```

---

### Acessando o número `6`

```python
print(matriz[2][1])
```

```text
linha 2 → [5, 6]
coluna 1 → 6
```

Resultado:

```text
6
```
