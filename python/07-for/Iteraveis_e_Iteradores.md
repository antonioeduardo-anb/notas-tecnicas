# iterador e for 
# o for percorre uma sequencia de elementos, como uma lista, tupla ou string, e executa um bloco de código para cada elemento da sequência., esse tipo de elemento é chamado de iteravel.
# um elemento iteravel é qualquer objeto que tem um metodo interno chamado __iter__() que retorna um iterador, que é um objeto que implementa o metodo __next__().

# 
# iteravel = objeto que pode ser percorrido, como listas, tuplas, strings, dicionarios,conjuntos, etc, todos esse objetos possuem o metodo __iter__() que retorna um iterador.

# iterador = quem sabe entregar um valor por vez, ele possui o metodo __next__() que  retorna o proximo valor da sequencia, quando não houver mais valores a serem entreges ele levanta a exceção StopIteration.

# next = me entrega o proximo valor do iterador.

palavra = "python".__iter__()
# palavra é um objeto iterador que possui o metodo __next__(), ele retorna o proximo valor da sequencia.
print(palavra)

# usando a função next() que é uma função que chama o metodo __next__() do objeto iterador.
print(next(palavra)) # p
print(next(palavra)) # y
print(next(palavra)) # t
print(next(palavra)) # h
print(next(palavra)) # o 
print(next(palavra)) # n   
#print(next(palavra)) # StopIteration


texto = "Antonio"
iterador = iter(texto) # chamando o metodo __iter__() do objeto iteravel texto, que retorna um objeto iterador.

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break   

     

