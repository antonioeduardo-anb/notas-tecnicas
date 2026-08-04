
# `while`

O `while` é uma estrutura de repetição (*loop*).

Ele executa um bloco de código repetidamente enquanto uma determinada condição for verdadeira.

## Sintaxe

```python
while condição:
    código
```

O funcionamento pode ser representado da seguinte forma:

```text
Verifica a condição.
          │
          ▼
A condição é verdadeira?
          │
    ┌─────┴─────┐
    │           │
   Sim         Não
    │           │
    ▼           ▼
Executa      Encerra
o bloco      o laço
    │
    └───────────┐
                │
                ▼
      Verifica novamente
```

---

## Exemplo 1: contador

Uma das utilizações mais comuns do `while` é a criação de contadores.

```python
contador = 1

while contador <= 5:
    print(f"Repetição número {contador}")
    contador += 1
```

Saída:

```text
Repetição número 1
Repetição número 2
Repetição número 3
Repetição número 4
Repetição número 5
```

---

## O que está acontecendo?

### Passo 1

```python
contador = 1
```

A variável recebe o valor `1`.

---

### Passo 2

```python
while contador <= 5:
```

O Python verifica se a condição é verdadeira.

```python
1 <= 5
```

O resultado é:

```python
True
```

---

### Passo 3

O bloco é executado.

```python
print(f"Repetição número {contador}")
contador += 1
```

O valor de `contador` passa a ser `2`.

---

### Passo 4

O processo se repete até que a condição seja falsa.

```python
6 <= 5
```

Resultado:

```python
False
```

Nesse momento, o laço é encerrado.

---

## Incremento

Esta linha:

```python
contador += 1
```

é apenas uma forma abreviada de escrever:

```python
contador = contador + 1
```

---

## Exemplo 2: validação de entrada

O `while` é muito utilizado para validar informações fornecidas pelo usuário.

```python
SENHA_MESTRE = "1234"
tentativa = ""

while tentativa != SENHA_MESTRE:
    tentativa = input("Digite a senha: ")

    if tentativa != SENHA_MESTRE:
        print("Senha incorreta. ❌")

print("Acesso concedido. ✅")
```

O programa continuará sendo executado até que a senha correta seja digitada.

---

## Laço infinito

Um dos erros mais comuns é criar uma condição que nunca se torna falsa.

```python
contador = 1

while contador <= 5:
    print(contador)
```

O problema é que o valor de `contador` nunca é alterado.

Como consequência, a condição continuará sendo verdadeira.

```python
1 <= 5
```

```python
True
```

```python
1 <= 5
```

```python
True
```

```python
1 <= 5
```

```python
True
```

...

Esse comportamento é chamado de **laço infinito** (*infinite loop*).

---

## `while` e `if`

As duas estruturas trabalham com condições, mas possuem objetivos diferentes.

| Estrutura | Função                              |
| --------- | ----------------------------------- |
| `if`      | Executa uma verificação.            |
| `while`   | Executa verificações repetidamente. |

---

Você também pode encontrar este padrão com bastante frequência:

```python
while True:
    comando = input("> ")

    if comando == "sair":
        break
```

Nesse caso, o laço continuará sendo executado até que o comando `break` seja encontrado. 🚀
