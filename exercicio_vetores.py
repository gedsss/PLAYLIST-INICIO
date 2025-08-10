# Exercicio times

times = []

for i in range(3):
    time = input('Digite o nome de um time: ')
    times.append(time)

for i in range(len(times)):
    for j in range(len(times)):
        if i != j:
            print(f'{times[i]} x {times[j]}')
print('\n')

# Exercicio provas

gabarito = []

for i in range(5):
    respostag = (input(f'Escreva a resposta da {i + 1} questao: '))
    gabarito.append(respostag)


alunos = []
notas = [] 

for i in range(3):
    nome = input(f'Digite o nome do aluno {i + 1}: ')
    respostas = []

    for j in range(5):
        resposta = (input(f'Digite a resposta para a questão {j + 1}: '))
        respostas.append(resposta)

    nota = 0
    for h in range(5):
        if respostas[h] == gabarito[h]:
            nota += 2

    alunos.append(nome)
    notas.append(nota)   

for l in range(len(alunos)):
    print(f'O aluno de nome {alunos[l]} tirou a nota {notas[l]}')

media = sum(notas) / len(notas)

print(f'A média da turma foi: {media}')
print('\n')

# Exercicio cinema

cadeiras = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10']

while True:

    print(cadeiras)
    print('\n')
    afirm = (input('Deseja reservar uma cadeira? S/N ')).strip().upper()

    if (afirm == 'S') or (afirm == 's'):
        cadeira = print('Qual número da cadeira que deseja reservar? ')
        if (cadeiras[cadeira] != 'X'):
            print('Cadeira reservada com sucesso!')
            cadeiras[cadeira] = 'X'
        if (cadeiras[cadeira] == 'X'):
            print('Cadeira ja reservada!')
    if(afirm == 'N') or (afirm == 'n'):
        print('Saindo...')
        break
    else:
        print('Escolha inválida!')




    


