cadeiras = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10']

while True:
    print("\nCadeiras disponíveis:")
    print(cadeiras)
    
    afirm = input('\nDeseja reservar uma cadeira? [S/N] ').strip().upper()

    if afirm == 'N':
        print('Saindo...')
        break

    elif afirm == 'S':
        cadeira = input('Digite o número da cadeira que deseja reservar (ex: B1): ').strip().upper()

        if cadeira in cadeiras:
            index = cadeiras.index(cadeira)
            cadeiras[index] = 'X'
            print(f'Cadeira {cadeira} reservada com sucesso!')
        else:
            print('Cadeira já reservada ou inválida.')

    else:
        print('Escolha inválida! Digite apenas "S" ou "N".')
