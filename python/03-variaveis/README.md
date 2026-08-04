
# Variáveis

Em Python, uma variável é um nome (ou identificador) associado a um objeto armazenado na memória.

De maneira simplificada, podemos imaginar a memória RAM como um conjunto de espaços capazes de armazenar dados, como números, textos e estruturas mais complexas. Cada um desses espaços possui um endereço.

Para acessar esses dados, utilizamos nomes que apontam para os objetos armazenados na memória. Esses nomes são chamados de variáveis.

Exemplo:

```python
nome = "Eduardo"
```

O que acontece internamente:

1. O interpretador encontra o valor `"Eduardo"`.

2. Como existem aspas, ele reconhece que se trata de uma sequência de caracteres (`str`).

3. Um objeto do tipo `str` é criado na memória.

4. O identificador `nome` passa a se referir a esse objeto.

Podemos representar isso da seguinte maneira:

```text
nome ─────► objeto str("Eduardo")
```

Ou, de forma mais detalhada:

```text
nome ─────► endereço 0xABC ─────► objeto str("Eduardo")
```

É importante observar que o tipo pertence ao objeto, e não à variável.

```python
nome = "Eduardo"
nome = 10
```

Após a segunda atribuição, a situação passa a ser a seguinte:

```text
nome ─────► objeto int(10)
```

O objeto `"Eduardo"` continua existindo temporariamente na memória, mas, se nenhuma referência apontar para ele, poderá ser removido posteriormente pelo *Garbage Collector*.

---

## Objetos e tipos

Em Python, praticamente tudo é um objeto:

* números;
* textos;
* listas;
* funções;
* classes.

Cada objeto possui informações próprias, como:

* o seu valor;
* o seu tipo;
* a sua posição na memória;
* a quantidade de referências que apontam para ele.

Uma representação conceitual seria algo semelhante a isto:

```text
objeto = {
    tipo: str,
    valor: "Eduardo"
}
```

Naturalmente, a estrutura interna real é muito mais complexa.

---

## Tipagem dinâmica

Python é uma linguagem de tipagem dinâmica.

Isso significa que o interpretador determina o tipo do objeto durante a execução do programa.

Por esse motivo, a mesma variável pode se referir a objetos de tipos diferentes ao longo do tempo:

```python
valor = 10
valor = "dez"
valor = 3.14
```

Isso não significa que o tipo do objeto mudou. Na realidade, a variável passou a apontar para objetos diferentes.

---

## Operações matemáticas

Também podemos armazenar o resultado de expressões matemáticas.

```python
ano_nascimento = 1999

salario = 2_000.00

idade_atual = 2025 - ano_nascimento
```

O interpretador executa a operação primeiro:

```python
2025 - 1999
```

Em seguida, ele associa o resultado à variável:

```python
idade_atual = 26
```
