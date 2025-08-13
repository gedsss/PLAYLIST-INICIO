produto = []
estoque = []
preco = []

def adcEstoque():
    while True:
        while True:
            nome = input('Digite o nome do item: ').upper()
            if nome.replace(" ", "").isalpha():
                produto.append(nome)
                break
            else:
                print('Nome não permitido!')
        print('-' * 30)

        while True:
            estoq = (input('Digite a quantidade do item: '))
            if estoq.isdigit():
                estoque.append(int(estoq))
                break
            else:
                print('Quantidade não permitida')
        print('-' * 30)

        while True:
            prec = (input('Digite o preço do item: '))
            if prec.isdigit():
                preco.append(int(prec))
                break
            else:
                print('Preco não permitido!')
        print('-' * 30)

        cont = input('Deseja adicionar outro item? [S/N] ').upper()
        if cont == 'N':
            print('Saindo...')
            print('-' * 30)
            break

def compra():

    valor_final = 0
    while True:
        cod = input('Digite o nome do produto: ').upper()
        if cod in produto:
            try:
                quant = int(input('Digite a quantidade do produto a ser comprado: '))
            except ValueError:
                print('Digite um número válido para a quantidade!')
                continue
            idx = produto.index(cod)
            if estoque[idx] >= quant:
                valor = preco[idx] * quant
                print(f'O Valor da compra ficará {valor}')
                estoque[idx] -= quant
                valor_final += valor
            else:
                print('Não há estoque suficiente.')
                print('-' * 30)
        else:
            print('O produto não consta no estoque.')
            print('-' * 30)

        cont = input('Deseja comprar outro item? [S/N] ').upper()
        if cont == 'N':
            print('Saindo...')
            print('-' * 30)
            break

    print('Qual forma de pagamento deseja utilizar?')
    print('1 - Pix (5% de desconto)')
    print('2 - Cartão (Débito ou Crédito)')
    print('3 - Dinheiro em espécie (2% de desconto)')
    while True:
        opcao = input('--- ')
        if opcao in ['1', '2', '3']:
            break
        else:
            print('Opção inválida')

    if opcao == '1':
        print(f'O valor final será de: {valor_final * 0.95}')
    elif opcao == '2':
        print(f'O valor final ficará de: {valor_final}')
    elif opcao == '3':
        print(f'O valor final ficará de: {valor_final * 0.98}')
    print('-' * 30)

def consultestoque():
    print('-' * 30)
    print('Produto | Estoque | Preço')

    for i in range(len(produto)):
        print(f'{produto[i]} | {estoque[i]} | {preco[i]}')
    print('-' * 30)

while True:
    print('-' * 30)
    print('MENU')
    print('-' * 30)
    print('1 - Para adicionar ao estoque')
    print('2 - Para consultar o estoque')
    print('3 - Para realizar uma compra')
    print('4 - Sair')
    escolha = input('---').strip()

    if escolha == '1':
        adcEstoque()
    elif escolha == '2':
        consultestoque()
    elif escolha == '3':
        compra()
    elif escolha == '4':
        print('Saindo do programa...')
        break
    else:
        print('Opção inválida!')





