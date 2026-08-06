def saudacao(msg):
    def saudar(nome):
        return f"{msg}, {nome}!"
    return saudar

nomes = ["Antonio", "Carlos", "Miguel"]

falar_bom_dia = saudacao("Bom dia")
falar_boa_tarde = saudacao("Boa tarde")
falar_boa_noite = saudacao("Boa noite")

for nome in nomes:
    print(falar_bom_dia(nome))
    print(falar_boa_tarde(nome))
    print(falar_boa_noite(nome))
