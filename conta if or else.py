from io import RawIOBase


print ('Seja bem vindo ao nosso site, faça o seu cadastro abaixo (não será aceito usuario e senha iguais')
usuário= str(input ('Digite aqui o seu usuário para o cadastro'))
senha= str(input ('Digite aqui a sua senha para o cadastro'))
if usuário==senha:
    print ('PAM, usuário igual a senha, tente novamente!')
    usuário= str(input ('Digite aqui o seu usuário para o cadastro'))
    senha= str(input ('Digite aqui a sua senha para o cadastro'))
else:
    print ('Cadastro feito com sucesso! Aproveite o nosso site!',)