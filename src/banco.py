saldo = 0
depositos = []
saques = []
saque_diario_count = 0
limite_diario_saques = 3
limite_valor_saque = 500


def depositar(valor):
    global saldo, depositos
    if valor > 0:
        depositos.append(valor)
        saldo += valor
        print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
    else:
        print('Valor de depósito inválido. Digite um valor positivo.')


def sacar(valor):
    global saldo, saques, saque_diario_count, limite_diario_saques, limite_valor_saque
    if valor > 0:
        if saque_diario_count < limite_diario_saques:
            if valor <= limite_valor_saque:
                if saldo >= valor:
                    saques.append(valor)
                    saldo -= valor
                    saque_diario_count += 1
                    print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
                else:
                    print('Saldo insuficiente para realizar o saque.')
            else:
                print(
                    f'Valor de saque excede o limite de R$ {limite_valor_saque:.2f}.')
        else:
            print('Limite diário de saques atingido.')
    else:
        print('Valor de saque inválido. Digite um valor positivo.')


def extrato():
    global saldo, depositos, saques
    if not depositos and not saques:
        print('Não foram realizadas movimentações.')
    else:
        print('\nExtrato:')
        if depositos:
            print('\nDepósitos:')
            for deposito in depositos:
                print(f'Depósito: R$ {deposito:.2f}')
            print('-' * 20)  # Linha pontilhada após depósitos
        if saques:
            print('\nSaques:')
            for saque in saques:
                print(f'Saque: R$ {saque:.2f}')
            print('-' * 20)  # Linha pontilhada após saques
        print(f'\nSaldo atual: R$ {saldo:.2f}')
