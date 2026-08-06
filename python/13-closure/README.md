
# Closures

Um *closure* ocorre quando:

* uma função é criada dentro de outra função;
* a função interna utiliza variáveis pertencentes à função externa;
* a função externa retorna a função interna.

Isso permite que a função interna continue acessando essas variáveis mesmo depois que a função externa terminar a sua execução.

---

## Estrutura básica

```python
def funcao_externa():
    variavel = "Olá"

    def funcao_interna():
        print(variavel)

    return funcao_interna
```

---

## Exemplo

```python
def fazer_saudacao(msg):

    def saudar(nome):
        return f"{msg} {nome}"

    return saudar
```

---

## O que está acontecendo?

Quando executamos:

```python
falar_bom_dia = fazer_saudacao("Bom dia")
```

o Python executa algo semelhante a isto:

```text
fazer_saudacao("Bom dia")
        │
        ▼
msg = "Bom dia"

def saudar(nome):
    return f"{msg} {nome}"

return saudar
```

A variável `msg` continua existindo porque a função `saudar()` ainda faz referência a ela.

---

## Representação visual

```text
falar_bom_dia
       │
       ▼
┌───────────────────┐
│ função saudar()   │
│ msg = "Bom dia"   │
└───────────────────┘
```

---

Agora vamos criar outro *closure*:

```python
falar_boa_noite = fazer_saudacao("Boa noite")
```

Teremos duas funções independentes:

```text
falar_bom_dia
       │
       ▼
┌───────────────────┐
│ função saudar()   │
│ msg = "Bom dia"   │
└───────────────────┘


falar_boa_noite
       │
       ▼
┌─────────────────────┐
│ função saudar()     │
│ msg = "Boa noite"   │
└─────────────────────┘
```

---

## Utilizando os *closures*

```python
print(falar_bom_dia("Eduardo"))
print(falar_boa_noite("Antonio"))
```

Resultado:

```text
Bom dia Eduardo
Boa noite Antonio
```

---

## Reutilizando a lógica

```python
nomes = [
    "Rodrigo",
    "Márcia",
    "Cíntia",
    "Mário"
]

for nome in nomes:
    print(f"{falar_bom_dia(nome)} 😄")
    print(f"{falar_boa_noite(nome)} 😴")
```

Resultado:

```text
Bom dia Rodrigo 😄
Boa noite Rodrigo 😴

Bom dia Márcia 😄
Boa noite Márcia 😴

Bom dia Cíntia 😄
Boa noite Cíntia 😴

Bom dia Mário 😄
Boa noite Mário 😴
```

---

## O que o *closure* está armazenando?

O *closure* não armazena apenas a função.

Ele também preserva:

* as variáveis utilizadas;
* o escopo onde a função foi criada;
* o estado daquele momento específico.

---

## Uma analogia

Imagine que a função interna seja uma mochila. 🎒

Quando ela é criada, coloca dentro da mochila tudo aquilo de que precisará no futuro. Depois, mesmo que a função externa desapareça, a mochila continua existindo e carregando esses dados.

---

## Relação com programação orientada a objetos

Curiosamente, um *closure* e uma classe podem resolver problemas semelhantes.

Por exemplo:

```python
class Saudacao:
    def __init__(self, msg):
        self.msg = msg

    def saudar(self, nome):
        return f"{self.msg} {nome}"
```

Nesse caso, o atributo `self.msg` desempenha um papel semelhante ao da variável `msg` do *closure*. 🚀
