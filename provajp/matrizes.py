def cria_matriz():
    n= int(input ('n de linhas: '))
    m= int(input ('n de colunas: '))
    matriz = []
    for i in range(n):
        linha = []
        for j in range(m):
            linha.append(int(input('Digite o valor de ['+ str(i) + ',' + str(j) + ']:')))
        matriz.append(linha)
#imprimir em formato de matriz
    for i in range(n):
        print(matriz[i])


matrix= cria_matriz()