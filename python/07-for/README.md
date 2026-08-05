
# `for`

O `for` é uma estrutura de repetição (*loop*) utilizada para percorrer elementos de um objeto iterável.

Diferentemente do `while`, o `for` é usado quando sabemos qual conjunto de elementos será percorrido.

Entre os objetos que podem ser percorridos estão:

* `str` (strings);
* `list` (listas);
* `tuple` (tuplas);
* `set` (conjuntos);
* `dict` (dicionários);
* `range`.

---

## Sintaxe

```python
for elemento in iteravel:
    código
```

O funcionamento pode ser representado da seguinte forma:

```text
iterável = [A, B, C]

         for
          │
          ▼
elemento = A
          │
          ▼
executa o bloco
          │
          ▼
elemento = B
          │
          ▼
executa o bloco
          │
          ▼
elemento = C
          │
          ▼
executa o bloco
          │
          ▼
fim do laço
```

---

## Exemplo 1: percorrendo uma string

Uma *string* é uma sequência de caracteres e, por isso, pode ser percorrida pelo `for`.

```python
texto = "Python"

for letra in texto:
    print(letra)
```

Saída:

```text
P
y
t
h
o
n
```

---

## O que está acontecendo?

O Python executa os seguintes passos:

```text
texto = "Python"

letra = "P"
letra = "y"
letra = "t"
letra = "h"
letra = "o"
letra = "n"
```

Observe que a variável `letra` assume um valor diferente a cada repetição.

---

# Exemplo 2: utilizando `range()`

A função `range()` cria um objeto iterável que produz uma sequência de números.

---

## Sintaxe

```python
range(início, fim, passo)
```

| Argumento | Função                       |
| --------- | ---------------------------- |
| `início`  | Primeiro valor da sequência. |
| `fim`     | Valor final (não incluído).  |
| `passo`   | Intervalo entre os números.  |

---

### Exemplo

```python
for numero in range(1, 11):
    print(numero)
```

Saída:

```text
1
2
3
4
5
6
7
8
9
10
```

---

### O que acontece internamente?

```python
range(1, 11)
```

produz algo semelhante a:

```text
1, 2, 3, 4, 5, 6, 7, 8, 9, 10
```

Observe que o último valor não é incluído.

```python
range(1, 11)
```

inclui o `1`, mas exclui o `11`.

---

## Exemplo 3: percorrendo listas

```python
frutas = ["banana", "maçã", "uva"]

for fruta in frutas:
    print(fruta)
```

Saída:

```text
banana
maçã
uva
```

---

## `break`

A instrução `break` interrompe completamente a execução do laço.

```python
frutas = ["banana", "maçã", "uva", "laranja"]

for fruta in frutas:
    if fruta == "uva":
        print("Encontrei a uva.")
        break

    print(fruta)
```

Fluxo de execução:

```text
banana
maçã
uva
↓
break
↓
fim do laço
```

---

## `continue`

A instrução `continue` interrompe apenas a repetição atual e passa imediatamente para a próxima.

```python
for numero in range(1, 6):
    if numero == 3:
        continue

    print(numero)
```

Saída:

```text
1
2
4
5
```

Fluxo de execução:

```text
1 → executa
2 → executa
3 → ignora
4 → executa
5 → executa
```

---

## `for` e `while`

As duas estruturas são laços de repetição, mas possuem finalidades diferentes.

| Estrutura | Utilização                                             |
| --------- | ------------------------------------------------------ |
| `for`     | Percorrer elementos de um iterável.                    |
| `while`   | Repetir uma ação enquanto uma condição for verdadeira. |

---

Uma forma simples de diferenciar os dois é a seguinte:

* `for` → "para cada elemento";
* `while` → "enquanto a condição for verdadeira".

Essa é a razão pela qual você verá o `for` sendo usado com muita frequência em listas, arquivos, dicionários e bancos de dados. 🚀
