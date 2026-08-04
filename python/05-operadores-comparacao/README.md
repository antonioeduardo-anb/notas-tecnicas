## Operadores de comparação

As condições normalmente utilizam operadores relacionais.

| Operador | Significado    |
| -------- | -------------- |
| `==`     | igual          |
| `!=`     | diferente      |
| `>`      | maior          |
| `<`      | menor          |
| `>=`     | maior ou igual |
| `<=`     | menor ou igual |

Exemplo:

```python
idade = 20

if idade == 20:
    print("Você tem 20 anos.")
```

---

## Operadores lógicos

Também é possível combinar várias condições.

### `and`

Retorna `True` quando todas as condições são verdadeiras.

```python
idade = 20
possui_documento = True

if idade >= 18 and possui_documento:
    print("Entrada permitida.")
```

---

### `or`

Retorna `True` quando pelo menos uma condição é verdadeira.

```python
if idade >= 60 or possui_prioridade:
    print("Atendimento prioritário.")
```

---

### `not`

Inverte o resultado da condição.

```python
usuario_logado = False

if not usuario_logado:
    print("Faça o login.")
```

---

## A importância da indentação

Em Python, os blocos de código são delimitados pela indentação.

```python
idade = 18

if idade >= 18:
    print("Maior de idade.")
```

Isto está incorreto:

```python
idade = 18

if idade >= 18:
print("Maior de idade.")
```

Isso acontece porque o Python utiliza os espaços no início das linhas para identificar a quais blocos de código cada instrução pertence.