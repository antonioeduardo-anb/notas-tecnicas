
# Fatiamento (*slicing*)

O fatiamento (*slicing*) é uma técnica utilizada para obter uma parte de uma sequência.

Entre as estruturas que podem ser fatiadas estão:

* listas (`list`);
* strings (`str`);
* tuplas (`tuple`).

O resultado do fatiamento é uma nova sequência contendo os elementos selecionados.

---

## Sintaxe

```python
sequencia[inicio:fim:passo]
```

| Parâmetro | Significado                   |
| --------- | ----------------------------- |
| `inicio`  | Índice inicial (incluído).    |
| `fim`     | Índice final (não incluído).  |
| `passo`   | Intervalo entre os elementos. |

---

## Exemplo básico

```python
letras = ["A", "B", "C", "D", "E"]

partes = letras[1:4]

print(partes)
```

Resultado:

```text
['B', 'C', 'D']
```

Representação visual:

```text
Índices

  0    1    2    3    4
┌───┬───┬───┬───┬───┐
│ A │ B │ C │ D │ E │
└───┴───┴───┴───┴───┘
      └─────────┘
         1:4
```

Observe que o índice `4` não é incluído.

---

## Por que o último índice não é incluído?

Essa decisão facilita vários cálculos.

Por exemplo:

```python
letras[1:4]
```

O tamanho da sequência pode ser calculado diretamente:

```python
4 - 1 = 3
```

Portanto, o resultado possui três elementos.

```text
B
C
D
```

---

## Omitindo o início

Se o índice inicial for omitido, o Python começará pelo primeiro elemento.

```python
inicio = letras[:3]
```

Resultado:

```text
['A', 'B', 'C']
```

```text
  0    1    2    3    4
┌───┬───┬───┬───┬───┐
│ A │ B │ C │ D │ E │
└───┴───┴───┴───┴───┘
└───────────┘
      :3
```

---

## Omitindo o final

Se o índice final for omitido, o Python continuará até o último elemento.

```python
fim = letras[2:]
```

Resultado:

```text
['C', 'D', 'E']
```

```text
  0    1    2    3    4
┌───┬───┬───┬───┬───┐
│ A │ B │ C │ D │ E │
└───┴───┴───┴───┴───┘
          └───────────┘
               2:
```

---

## Utilizando o passo

O terceiro valor determina quantos elementos serão pulados.

```python
saltando = letras[0:5:2]
```

Resultado:

```text
['A', 'C', 'E']
```

Representação:

```text
  0    1    2    3    4
┌───┬───┬───┬───┬───┐
│ A │ B │ C │ D │ E │
└───┴───┴───┴───┴───┘
  ▲         ▲         ▲
```

---

## Índices negativos

Também podemos percorrer a sequência de trás para a frente.

```python
letras = ["A", "B", "C", "D", "E"]
```

```text
 Índices positivos

   0    1    2    3    4
┌───┬───┬───┬───┬───┐
│ A │ B │ C │ D │ E │
└───┴───┴───┴───┴───┘
  -5  -4  -3  -2  -1

 Índices negativos
```

Exemplo:

```python
print(letras[-3:])
```

Resultado:

```text
['C', 'D', 'E']
```

---

## Invertendo uma sequência

Também é possível utilizar um passo negativo.

```python
invertida = letras[::-1]
```

Resultado:

```text
['E', 'D', 'C', 'B', 'A']
```
