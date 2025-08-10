while True:
    try:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        break
    except ValueError:
        print('Por favor digite números válidos')


if n1 < n2:
    for i in range(n1, n2 + 1):
        print(i)
if n1 > n2:
    for i in range(n1, n2 - 1, -1):
        print(i)
  
# Exercicio de notas

while True:
    try:
        alunos = int(input('Quantos alunos a escola possui? '))
        break
    except ValueError:
        print('Digite um número valido!')


melhor = 0
nome = ''

for i in range(alunos):

    while True:
            alunoN = input('Digite o nome do aluno: ')

            if alunoN.isalpha():
                break
            else:
                print('Digite um nome válido!')

    
    while True:
        try:
            nota = float(input('Digite a nota do aluno: '))
            
            if (nota <= 10) and (nota >= 0):
                break
            else:
                print('Digite uma nota válida!')
            
        except ValueError:
            print('Digite uma nota válida!')

    if nota > melhor:
        melhor = nota 
        nome = alunoN

print(f'O melhor aluno foi {nome} com a nota de {melhor}')

# Exercicio super contador 

while(True):
    print('Digite 1 para contar de 1 a 10')
    print('Digite 2 para contar de 10 a 1')
    print('Digite 3 para sair')
    menu = float(input(''))

    if menu == 1:
        for i in range(1, 11):
            print(i)

    elif menu == 2:
        for i in range(10, 0, -1):
            print(i)
    elif menu == 3:
        break
print('\n')

# Exercicio de pessoas

h = 0
m = 0

while True:
    sexo = (input('Digite o sexo: [M/F] ')).strip().upper()
    idade = int(input('Digite a idade: '))
    cabelo = (input('Digite a cor do cabelo: (Preto, Castanho, Loiro, Ruivo) '))
    cont = int(input('Digite 1 caso queira continuar e 2 caso não queira: '))

    if(cont == 2):
        break
    if (sexo == 'M') and (idade > 18) and (cabelo == 'Castanho'):
        h += 1
    elif (sexo == 'F') and (idade >= 25 and idade <= 30) and (cabelo == 'Loiro'):
        m += 1
    

print(h)
print(m)
print('\n')

# Exercicio usando valores

soma = 0
media = 0
div5 = 0
nulo = 0
soma_par = 0

for i in range(5):
    num = int(input('Digite um valor: '))

    soma += num

    if num % 5 == 0:
        div5 += 1
    if num == 0:
        nulo += 1   
    if num % 2 == 0:
        soma_par += num

media = soma / 5

print(f'Soma dos números: {soma}')
print(f'Media dos números: {media}')
print(f'Valores divisiveis por 5: {div5}')
print(f'Valores nulos: {nulo}')
print(f'Soma dos valores pares: {soma_par}')


    


    
