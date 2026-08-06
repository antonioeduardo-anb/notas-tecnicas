nomes = ["Antonio", "Carlos", "Miguel"]

n1, n2, n3 = nomes

print(n1)
print(n2)
print(n3)

# Agrupar varios valores em uma unica variavel  
primeiro, *resto = nomes
print(primeiro)
print(resto)

# Desempacotando listas aninhadas
dados = ["Eduardo", [10,20,30]]
nome, numero = dados
print(nome)
print(numero)

