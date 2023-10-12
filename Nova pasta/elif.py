nome= str(input ('Qual é o seu nome? '))
if nome== 'Daniel':
    print ('Que bosta hein')
elif nome == 'Vitor' or nome== 'Yasmin' or nome== 'Fátima':
    print ('Nomin bons hein')
else:
    print ('Você merece a morte, {}.'.format(nome))
print ('Tenha um bom dia, {}.'.format(nome))