print ('Bem vindo ao simulador de aprovação de empréstimo!, preencha os dados a seguir e veja se você é aprovado')
valor= float(input('Digite o valor do que você quer comprar'))
salario= float(input ('Digite o seu salário'))
anos= int(input ('Digite em quantos anos vc pretende pagar'))
prestação= valor/(anos*12)
if prestação > (30/100)*valor:
    print ('Liso pra porra, vai dar certo não.')
else:
    print('Seu empréstimo seria aprovado e a prestação seria de: R$:'.format(prestação))