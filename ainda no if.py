nome= str(input ('Digite aqui seu nome'))
if nome == 'Daniel':
    print ('Que nome bosta hein')
else:import sys
sys.setrecursionlimit(1500)

def somatorio(x): #chamei a função pra fazer o somatório (utilizei de função recursiva)
    if x==1:
        return 1
    else:
        return x + somatorio(x-1)
#aqui armazena os dados das variáveis pra realizar o somatório
while True:
    a= float(input ('numero a: '))
    b= float(input ('numero b: '))
    c= int(input ('numero c: '))
    if c==0:  #e esse if impede que o usuario de 0 como valor pra c pedindo pra que ele digite novamente os valores pra fazer o somatório direitinho
        print('PAM, digite um número válido pra C')
    else: #aí caso não caia no if ele faz direto o cálculo
        x = a+b+c 
        print("F(x)= ",somatorio(x) )
    
    print ('nossa muito foda parabens')
print ('valeu seu MERDA')        