
# Estruturas condicionais (`if`, `elif` e `else`)

As estruturas condicionais permitem que o programa tome decisões com base em determinadas condições.

Em outras palavras, o Python avalia uma expressão e decide qual bloco de código deve ser executado.

A estrutura básica é composta por três elementos:

* `if` ("se");
* `elif` ("senão, se");
* `else` ("senão").

---

## `if`

O `if` executa um bloco de código apenas se a condição for verdadeira.

### Sintaxe

```python
if condição:
    código
```

### Exemplo

```python
idade = 20

if idade >= 18:
    print("Maior de idade.")
```

---

## `else`

O `else` é executado quando a condição do `if` é falsa.

### Sintaxe

```python
if condição:
    código
else:
    código
```

### Exemplo

```python
idade = 16

if idade >= 18:
    print("Maior de idade.")
else:
    print("Menor de idade.")
```

---

## `elif`

`elif` significa **"else if"** ("senão, se").

Ele permite testar uma nova condição caso a anterior seja falsa.

### Sintaxe

```python
if condição:
    código

elif outra_condição:
    código

else:
    código
```

### Exemplo

```python
nota = 8

if nota >= 9:
    print("Excelente!")

elif nota >= 7:
    print("Você passou!")

elif nota >= 5:
    print("Recuperação.")

else:
    print("Reprovado.")
```

---

## Como o Python executa as condições

O interpretador analisa as condições de cima para baixo.

```text
if
 │
 ▼
A condição é verdadeira?
 │
 ├── Sim ──► Executa o bloco.
 │
 └── Não ──► Verifica o próximo elif.
                 │
                 ▼
         A condição é verdadeira?
                 │
                 ├── Sim ──► Executa o bloco.
                 │
                 └── Não ──► Continua.
                                  │
                                  ▼
                                else
```

Quando o Python encontra a primeira condição verdadeira, a busca é interrompida.

Por exemplo:

```python
nota = 8

if nota >= 9:
    print("Excelente!")

elif nota >= 7:
    print("Aprovado!")

elif nota >= 5:
    print("Recuperação!")

else:
    print("Reprovado!")
```

A execução ocorre da seguinte maneira:

```text
nota >= 9  → falso

nota >= 7  → verdadeiro

nota >= 5  → ignorado

else       → ignorado
```

Resultado:

```text
Aprovado!
```

---



---

Uma curiosidade interessante é que, internamente, uma cadeia de `if`, `elif` e `else` se parece muito com uma árvore de decisões. 🌳
