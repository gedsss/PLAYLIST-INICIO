# SISTEMA DE LIVRARIA

livros = ['livro0', 'livro1', 'livro3']

while True:

    print('-' * 30)
    print('Digite 1 para alugar um livro')
    print('Digite 2 para devolver um livro')
    print('Digite 3 para verificar o estoque de livros')
    print('Digite 4 para sair')
    menu = int(input('Digite uma das opções: '))
    print('-' * 30)

    if menu == 1:
        if livros:
            print('Livros disponíveis: ', livros)
            while True:
                escolha = input('Digite o livro que deseja alugar: ')
                if escolha not in livros:
                    print('Digite um livro válido')
                if escolha in livros:
                    print('Livro alugado com sucesso!')
                    livros.remove(escolha)
                    break
        else:
            print('Não há livros disponíveis!')
    
    if menu == 2:
        devolv = input('Digite o nome do livro que deseja devolver: ')
        livros.append(devolv)
        print('Livro devolvido com sucesso!')

    if menu == 3:
        print('O estoque atual de livros é de: ')
        print(livros)
    
    if menu == 4:
        print('Saindo...')
        break
