a= float(input('a: ')) #aqui pede os numeros
b= float(input('b: '))
while True: #e o laço while aqui não permite que o c seja zero
    c= int(input('c: '))
    if c==0:
        print('ERRO!!! O c não pode ser zero, digite novamente o c: ')
    else:
        break

s= int((a+b)/c) #aqui vê qual que é o valor pra fazer o somatório feito o calculo do somatório

v= 0 
for i in range(s+1): #e aqui é feito o calculo do somatório
    v= i + v

print ('F(x)=', v) #aqui mostra o resultado