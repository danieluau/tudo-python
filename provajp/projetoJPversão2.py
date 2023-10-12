def somarMatrizes(matrizA, matrizB):
    if(len(matrizA) != len(matrizB) or len(matrizA[0]) != len(matrizB[0])):
        return None
    result = []
    for i in range(len(matrizA)):   
        result.append([])
        for j in range(len(matrizB[0])):
            result[i].append(matrizA[i][j] + matrizB[i][j])
    return result

def matriz_nula(n):
    matriz = []
    for linha in range(n):
        matriz.append([])
        for coluna in range(n):
            matriz[linha].append(0)
    return matriz

def transposta(matriz):
    nova_matriz = matriz_nula(len(matriz))
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):
             nova_matriz[coluna][linha] = matriz[linha][coluna]
    return nova_matriz

def diagonal(matriz):
    nova_matriz = matriz_nula(len(matriz))
    for i in range(len(matriz)):
        nova_matriz[i][i] = matriz[i][i]
    return nova_matriz

def mat_mul (A, B):
    num_linhas_A, num_colunas_A = len(A), len(A[0])
    num_linhas_B, num_colunas_B = len(B), len(B[0])
    assert num_colunas_A == num_linhas_B

    C= []
    for linha in range(num_linhas_A):
        C.append([])
        for coluna in range(num_colunas_B):
            C[linha].append(0)
            for k in range(num_colunas_A):
                C[linha][coluna] += A[linha][k] * B[k][coluna]
    return C    


nA= int(input ('n de linhas de a: '))
matrizA = []
for i in range(nA):
    # linhaA = []
    # for j in range(nA):
    #     linhaA.append(int(input('Digite o valor de ['+ str(i) + ',' + str(j) + ']:')))
    linhaA = input('Digite a linha ' + str(i + 1) + ':').split()
    for i in range(len(linhaA)):
        linhaA[i] = int(linhaA[i])
    matrizA.append(linhaA)


nB= int(input ('n de linhas de b: '))
matrizB = []
for i in range(nB):
    # linhaB = []
    # for j in range(nB):
    #     linhaB.append(int(input('Digite o valor de ['+ str(i) + ',' + str(j) + ']:')))
    linhaB = input('Digite a linha ' + str(i + 1) + ':').split()
    for i in range(len(linhaB)):
        linhaB[i] = int(linhaB[i])
    matrizB.append(linhaB)

#imprimir em formato de matriz
print('Matriz A: ')
for i in range(nA):
    print(*matrizA[i])
print()
print('Matriz B: ')    
for i in range(nB):
    print(*matrizB[i])
print()

d= diagonal(matrizB)
mult= mat_mul(d, matrizB)
trans= transposta(matrizA)
r= somarMatrizes(trans, mult)
print('Matriz R: ')
for i in range(len(r)):
    print(*r[i])
print()
