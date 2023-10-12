def transpostaMatriz(m):
    return list(map(lambda *c: [l for l in c], *m)) #leitura e transposição


matriz = [[1,2,3], [4, 5, 6],[7,8,9]] #matriz

print(transpostaMatriz(matriz)) #printa transposta


