from src.banco import depositar, sacar, extrato


def menu():
    while True:
        print('\nMenu:\n')
        print('1. Depositar')
        print('2. Sacar')
        print('3. Extrato')
        print('4. Sair')

        escolha = input('\nEscolha uma opção: ')

        if escolha == '1':
            valor = float(input('\nDigite o valor do depósito: '))
            depositar(valor)
        elif escolha == '2':
            valor = float(input('\nDigite o valor do saque: '))
            sacar(valor)
        elif escolha == '3':
            extrato()
        elif escolha == '4':
            print('\nSaindo do programa...')
            break
        else:
            print('\nOpção inválida. Por favor, escolha uma opção válida.')


if __name__ == '__main__':
    menu()
