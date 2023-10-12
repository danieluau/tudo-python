palavras= (input ('Digite as palavras: '))
sep= palavras.split()   #o split aqui separa as palavras
lis= sorted(sep)        #o sorted organiza as palavras por ordem alfabética
print ("".join(lis))    #e o join junta tudo e como tá dentro do print
