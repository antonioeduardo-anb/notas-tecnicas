
# Tipos de dados

Os tipos de dados podem ser entendidos como uma classificação utilizada pelo Python para representar valores na memória e definir quais operações podem ser realizadas sobre eles.

Em outras palavras, o tipo de dado determina como o interpretador deve tratar determinada informação.

Por exemplo, o valor literal `2` é interpretado como um número inteiro e pertence ao tipo `int` (*integer*).

```python
2
```

Já `"Antonio"` é interpretado como uma sequência de caracteres Unicode e pertence ao tipo `str` (*string*).

```python
"Antonio"
```

Outros exemplos:

* `True` → valor lógico pertencente ao tipo `bool`.

* `int` → números inteiros.

```python
10
```

* `float` → números de ponto flutuante.

```python
1.15
```

* `str` → sequência de caracteres.

```python
"Eduardo"
```

* `bool` → valores lógicos (`True` ou `False`).

```python
True
False
```

* `list` → coleção ordenada e mutável de elementos.

```python
["banana", "laranja", "maçã"]
```

* `tuple` → coleção ordenada e imutável de elementos.

```python
("a", 1)
```

* `dict` → coleção de pares formados por uma chave e um valor.

```python
{"chave": "valor"}
```

* `set` → coleção mutável de elementos únicos.

```python
{"a", "b", "c"}
```

* `None` → representa a ausência de um valor.

```python
None
```

Esses são alguns dos principais tipos de dados nativos da linguagem. O interpretador do Python reconhece todos eles sem a necessidade de bibliotecas externas.

`list`, `tuple`, `dict` e `set` também são conhecidos como estruturas de dados ou tipos de coleção.

---

Uma observação importante é que, em Python, praticamente tudo é um objeto:

```python
type(2)
# <class 'int'>

type("Antonio")
# <class 'str'>

type(True)
# <class 'bool'>
```
