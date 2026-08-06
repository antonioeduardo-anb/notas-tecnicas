
# Dicionários (`dict`)

Os dicionários são estruturas de dados utilizadas para armazenar informações na forma de pares de **chave** e **valor**.

Em vez de acessar um elemento por meio de um índice numérico, como acontece nas listas, utilizamos uma chave.

---

## Estrutura

```python
chave: valor
```

---

## Características

Os dicionários:

* armazenam pares de chave e valor;
* preservam a ordem de inserção dos elementos;
* permitem modificar os valores armazenados;
* não permitem chaves duplicadas;
* permitem armazenar diferentes tipos de dados.

---

## Criando um dicionário

Os dicionários são delimitados por chaves (`{}`).

```python
pessoa = {
    "nome": "Antonio",
    "sobrenome": "Barros",
    "idade": 36
}
```

Representação:

```text
pessoa
│
├── nome ───────► Antonio
├── sobrenome ─► Barros
└── idade ─────► 36
```

---

## Acessando valores

Podemos acessar os elementos utilizando suas chaves.

```python
print(pessoa["nome"])
print(pessoa["idade"])
```

Resultado:

```text
Antonio
36
```

---

## Dicionários aninhados

Um dicionário pode conter outros dicionários, listas, tuplas e diversos tipos de objetos.

```python
pessoa = {
    "nome": "Antonio",
    "sobrenome": "Barros",
    "idade": 36,
    "enderecos": [
        {
            "rua": "Vitória",
            "numero": 110
        },
        {
            "rua": "Silva",
            "numero": 230
        }
    ]
}
```

Representação:

```text
pessoa
│
├── nome
├── sobrenome
├── idade
└── enderecos
    │
    ├── rua
    └── numero
```

---

## Criando e alterando elementos

Os dicionários são estruturas mutáveis.

Por isso, podemos adicionar ou modificar valores.

```python
pessoa["cidade"] = "Belford Roxo"
```

Se a chave não existir, ela será criada.

```text
cidade ───► Belford Roxo
```

---

Se a chave já existir, o valor será substituído.

```python
pessoa["cidade"] = "Rio de Janeiro"
```

Resultado:

```text
cidade ───► Rio de Janeiro
```

---

## Removendo elementos

Podemos utilizar a palavra-chave `del`.

```python
del pessoa["cidade"]
```

Também é possível verificar se a chave existe antes da remoção.

```python
if "cidade" in pessoa:
    del pessoa["cidade"]
```

---

## O método `get()`

Ao tentar acessar uma chave inexistente, o Python gera um erro.

```python
print(pessoa["profissao"])
```

Resultado:

```text
KeyError
```

Para evitar esse problema, utilizamos o método `get()`.

```python
profissao = pessoa.get(
    "profissao",
    "Não informada"
)
```

Resultado:

```text
Não informada
```

---

## Chaves dinâmicas

Uma das características mais interessantes dos dicionários é a possibilidade de criar chaves dinamicamente.

```python
campo = "tecnologia"

pessoa[campo] = "Python"
```

Resultado:

```text
tecnologia ───► Python
```

Isso é extremamente útil quando os nomes das chaves vêm de:

* formulários;
* bancos de dados;
* arquivos;
* entradas do usuário.

---

## Percorrendo um dicionário

## Percorrendo as chaves

```python
for chave in pessoa:
    print(chave)
```

---

## Percorrendo os valores

```python
for valor in pessoa.values():
    print(valor)
```

---

## Percorrendo as chaves e os valores

```python
for chave, valor in pessoa.items():
    print(chave, valor)
```

---

## Métodos importantes

| Método     | Função                          |
| ---------- | ------------------------------- |
| `get()`    | Obtém um valor.                 |
| `keys()`   | Retorna as chaves.              |
| `values()` | Retorna os valores.             |
| `items()`  | Retorna as chaves e os valores. |
| `pop()`    | Remove um elemento.             |
| `update()` | Atualiza o dicionário.          |
| `clear()`  | Remove todos os elementos.      |

---

## Chaves e índices

Essa é a principal diferença entre listas e dicionários:

| Estrutura  | Forma de acesso   |
| ---------- | ----------------- |
| Lista      | Índices numéricos |
| Dicionário | Chaves            |

Exemplo:

```python
lista = ["A", "B", "C"]

print(lista[0])
```

```python
dicionario = {
    "nome": "Antonio"
}

print(dicionario["nome"])
```

---

Uma forma simples de visualizar isso é imaginar uma lista telefônica. ☎️

Você não procura a informação pela posição em que ela está armazenada. Em vez disso, procura pelo nome da pessoa, que funciona como a chave do dicionário.
