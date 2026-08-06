
# Funções (`def`)

As funções são blocos de código reutilizáveis criados para executar tarefas específicas.

Elas permitem:

* reutilizar código;
* evitar repetições;
* tornar o programa mais organizado;
* facilitar a manutenção;
* dividir problemas complexos em partes menores.

Esse conceito está relacionado ao princípio **DRY** (*Don't Repeat Yourself*), que significa "não se repita".

---

## Por que utilizar funções?

Sem funções:

```python
print("Olá, Eduardo!")
print("Olá, Carlos!")
print("Olá, João!")
```

Com funções:

```python
def saudar(nome):
    print(f"Olá, {nome}!")

saudar("Eduardo")
saudar("Carlos")
saudar("João")
```

---

## Criando uma função

As funções são criadas com a palavra-chave `def`.

## Sintaxe

```python
def nome_da_funcao():
    código
```

Exemplo:

```python
def saudacao():
    print("Olá!")
```

---

# Chamando uma função

Criar uma função não significa executá-la.

Para executá-la, devemos chamá-la pelo seu nome.

```python
def saudacao():
    print("Olá!")

saudacao()
```

Resultado:

```text
Olá!
```

---

## Parâmetros e argumentos

Esses dois conceitos costumam ser confundidos.

## Parâmetros

São as variáveis declaradas na definição da função.

```python
def saudar(nome, idade):
    pass
```

Nesse exemplo, `nome` e `idade` são parâmetros.

---

## Argumentos

São os valores fornecidos durante a chamada da função.

```python
saudar("Antonio", 36)
```

Nesse caso:

| Argumento   | Parâmetro |
| ----------- | --------- |
| `"Antonio"` | `nome`    |
| `36`        | `idade`   |

---

## Exemplo completo

```python
def saudar(nome, idade):
    print(f"Olá, {nome}.")
    print(f"Você tem {idade} anos.")

saudar("Antonio", 36)
```

---

## O que acontece internamente?

O Python executa algo semelhante a isto:

```python
nome = "Antonio"
idade = 36
```

Em seguida, o corpo da função é executado.

---

# Valores padrão (*default values*)

Os parâmetros podem possuir valores predefinidos.

```python
def conexao(ip, porta=8080):
    print(f"IP: {ip}")
    print(f"Porta: {porta}")
```

Agora podemos chamar a função de duas maneiras:

```python
conexao("192.168.0.1")
```

Resultado:

```text
IP: 192.168.0.1
Porta: 8080
```

---

Também podemos fazer isto:

```python
conexao("192.168.0.1", 443)
```

Resultado:

```text
IP: 192.168.0.1
Porta: 443
```

---

## Regra importante

Os parâmetros com valores padrão devem aparecer depois dos parâmetros obrigatórios.

✔ Correto:

```python
def conexao(ip, porta=8080):
    pass
```

❌ Incorreto:

```python
def conexao(porta=8080, ip):
    pass
```

---

## Retorno (`return`)

O comando `return` encerra a execução da função e devolve um valor ao local onde ela foi chamada.

---

## Exemplo

```python
def soma(a, b):
    return a + b

resultado = soma(10, 20)

print(resultado)
```

Resultado:

```text
30
```

---

## O que acontece internamente?

```python
resultado = soma(10, 20)
```

O Python executa:

```python
a = 10
b = 20
```

Em seguida:

```python
return a + b
```

O resultado retornado será:

```python
30
```

---

## Exemplo: área de um círculo

```python
def calcular_area_circulo(raio):
    return 3.1415 * (raio ** 2)

area = calcular_area_circulo(5)

print(area)
```

Resultado:

```text
78.5375
```

---

## `return` e `print()`

Esses conceitos são diferentes.

| Comando   | Função                                         |
| --------- | ---------------------------------------------- |
| `print()` | Exibe informações na tela.                     |
| `return`  | Devolve um valor para outra parte do programa. |

---

### Exemplo com `print()`

```python
def soma(a, b):
    print(a + b)
```

---

### Exemplo com `return`

```python
def soma(a, b):
    return a + b
```

---

## Argumentos nomeados

Também é possível especificar explicitamente o nome dos parâmetros.

```python
def cadastrar(nome, idade):
    print(nome, idade)

cadastrar(idade=25, nome="Eduardo")
```

---

## Quantidade variável de argumentos

## `*args`

Permite receber vários argumentos posicionais.

```python
def soma(*numeros):
    print(numeros)

soma(1, 2, 3, 4)
```

Resultado:

```text
(1, 2, 3, 4)
```

Observe que `args` é uma tupla.

---

## `**kwargs`

Permite receber argumentos nomeados.

```python
def exibir(**dados):
    print(dados)

exibir(nome="Eduardo", idade=25)
```

Resultado:

```text
{
    "nome": "Eduardo",
    "idade": 25
}
```

Observe que `kwargs` é um dicionário.

---

## Docstrings

As *docstrings* são utilizadas para documentar o funcionamento das funções.

```python
def soma(x, y):
    """
    Soma dois números.

    Parâmetros:
        x: primeiro número.
        y: segundo número.

    Retorno:
        resultado da soma.
    """

    return x + y
```

---

## Escopo

As variáveis criadas dentro de uma função pertencem ao escopo local.

```python
def exemplo():
    mensagem = "Olá"

print(mensagem)
```

Resultado:

```text
NameError
```

Isso acontece porque `mensagem` existe apenas dentro da função.

---

## Uma função deve fazer apenas uma tarefa

❌ Exemplo ruim:

```python
def sistema():
    conectar()
    cadastrar()
    gerar_relatorio()
    enviar_email()
```

✔ Exemplo melhor:

```python
def conectar():
    ...

def cadastrar():
    ...

def gerar_relatorio():
    ...

def enviar_email():
    ...
```

Essa abordagem torna o código mais legível, reutilizável e fácil de manter. 🚀
