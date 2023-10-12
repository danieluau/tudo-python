carros = {} #aqui guarda os dados de placa, entrada e saida.

while True:
    opcao = int(input('Opção (1 - Cadastrar veiculo | 2 - Calcular taxa): '))
    if opcao == 1:
        HE, ME, SE = input('Digite a entrada no formato "hh:mm:ss": ').split(':')
        HE, ME, SE = int(HE), int(ME), int(SE)

        HS, MS, SS = input('Digite a saida no formato "hh:mm:ss": ').split(':')
        HS, MS, SS = int(HS), int(MS), int(SS)

        placa = input('Digite a placa: ')

        carros[placa] = [[HE, ME, SE], [HS, MS, SS]]

    elif opcao == 2: #aqui vai a parte de calculo.
        placa = input('Digite a placa: ')

        if placa not in carros:
            print('Não existe carro com essa placa cadastrada')
        else:
            info_entrada, info_saida = carros[placa]
            HE, ME, SE = info_entrada
            HS, MS, SS = info_saida

            minutos_entrada = HE * 60 + ME
            minutos_saida = HS * 60 + MS

            minutos_estacionado = minutos_saida - minutos_entrada

            preco = 0

            if minutos_estacionado <= 15:
                preco = 0
            elif minutos_estacionado <= 60:
                preco = 0.09 * (minutos_estacionado - 15)
            elif minutos_estacionado <= 120:
                # Taxa de 16 min até 60 min
                preco = 0.09 * (60 - 15)
                # + Taxa de 60 min até o tempo total (que é menor ou igual a 120 min)
                preco = preco + 0.12 * (minutos_estacionado - 60)
            else:
                # Taxa de 16 min até 60 min
                preco = 0.09 * (60 - 15)
                # + Taxa de 60 min até 120 min
                preco = preco + 0.12 * (120 - 60)
                # + Taxa final por passar de 120 min 0.2
                preco = preco + 0.2

            print(preco)
