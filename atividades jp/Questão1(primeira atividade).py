#tive ajuda do francisco nessa

a = input("a: ")
b = input("b: ")

# pra detectar qual numero é fracionario é só saber qual dos inputs pode ser
# separado em 2 por um ponto
if len(a.split(".")) == 2:
    numero_fracionario = a
    numero_inteiro = b
else:
    numero_fracionario = b
    numero_inteiro = a

# A parte fracionária é a parte depois do ponto, então p.e.:
# # se numero_fracionario for a string "23.792":
# numero_fracionario.split(".") resulta na lista ["23", "792"]
# numero_fracionario.split(".")[1] vai resultar no elemento "792" porque ele é
# o elemento na posição 1
parte_fracionaria_na_potencia_de_dez = numero_fracionario.split(".")[1]

# Por fim, é preciso converter pra inteiro pra de fato termos um numero em vez
# de string.
# Isso não precisa ser multiplicado por potencia de 10 porque como começa com
# "0." é como se essa conta já tivesse sido feita
parte_fracionaria_na_potencia_de_dez = int(parte_fracionaria_na_potencia_de_dez)

numero_inteiro = int(numero_inteiro)

quantidade_de_digitos_fracionarios = len(str(parte_fracionaria_na_potencia_de_dez))
potencia_de_dez = 10 ** quantidade_de_digitos_fracionarios

numero_inteiro_na_potencia_de_dez = numero_inteiro * potencia_de_dez

# Linguagens de programação não conseguem calcular bem contas fracionarias
# porque computadores usam base binaria enquanto a gente usa base decimal.
# Pra resolver isso, a melhor forma de fazer uma conta fracionaria ter precisão
# é multiplicando todos os números da conta por uma potencia de 10 que torne
# todos eles números inteiros, em seguida fazer as operações (menos, mais,
# divisão, etc...) e depois dividir o resultado pela mesma potência de 10

resultado = numero_inteiro_na_potencia_de_dez - parte_fracionaria_na_potencia_de_dez
resultado = resultado / potencia_de_dez

print(resultado)