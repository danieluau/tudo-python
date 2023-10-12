def somaLetras(s):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    valores = []
    for caractere in s:
        if caractere.isnumeric():
            valores.append(int(caractere))
        else:
            valores.append(alfabeto.find(caractere.lower()) + 1)
    return sum(valores)

str= input('str: ')
print (somaLetras(str))  