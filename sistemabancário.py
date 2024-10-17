saldo = 0
LIMITE_SAQUES_DIARIOS = 3
extrato = " "
numero_saques = 0
limite = 500
opção = 0

while True:
    print('''MENU: 
    [ 1 ] SAQUE 
    [ 2 ] EXTRATO
    [ 3 ] DEPÓSITO
    [ 4 ] SAIR''')
    opção = int(input('Qual opção você deseja? '))
    if opção == 1:
        valor = int(input('Quanto você quer sacar? R$'))
        saldo_excedido = valor > saldo
        limite_excedido = valor > limite
        saque_excedido = numero_saques >= LIMITE_SAQUES_DIARIOS

        if saldo_excedido:
            print('Você não tem saldo suficiente.')
                
        elif limite_excedido:
                print('Valor do saque excedeu o limite.')

        elif saque_excedido:
                print('Limite de saque excedido')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque realizado valor: R${valor:.2f}'
            numero_saques += 1
        else: 
            print('Operação falhou. Valor inválido')

    elif opção == 2:
        print('=-'*30)
        print('Não houve movimentações.' if not extrato else extrato)
        print(f'Saldo: R${saldo:.2f}')
        print('=-'*30)

    elif opção == 3:
        valor = float(input('Quanto você quer depositar? R$'))
        if valor > 0:
            saldo += valor
            extrato += f'Transação completa. Valor de R${valor:.2f}.\n'
        else:
            print('Operação inválida.')
    elif opção == 4:
        print('Volte sempre!')
        break
    else: 
        print('Operação não identificada! Selecione novamente a opção desejada')


