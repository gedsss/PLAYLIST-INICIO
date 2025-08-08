# Exercicio funções matrizes

import numpy as np

matriz = np.array([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
])

diagonal = np.diagonal(matriz)

trisup = np.triu(matriz)
tribel = np.tril(matriz)

for linha in matriz:
    print(linha)
print('\n')

print(diagonal)
print('\n')
print(trisup)
print('\n')
print(tribel)
print('\n')

# Exercicio Jogo da Velha

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

def verificar_vitoria(jogador):
    for linha in matriz:
        if all(item == jogador for item in linha):
            return True

    for col in range(3):
        if all(matriz[linha][col] == jogador for linha in range(3)):
            return True

    if all(matriz[i][i] == jogador for i in range(3)):
        return True
    if all(matriz[i][2 - i] == jogador for i in range(3)):
        return True

    return False

while True:
    while True:
        for i in matriz:
            for l in i:
                print(l, end=' ')
            print()
        
        escolha = int(input('Escolha uma posição para O: '))
        jogada_valida = False
        
        for i in range(3):
            for l in range(3):
                if matriz[i][l] == escolha:
                    matriz[i][l] = 'O'
                    jogada_valida = True
        
        if jogada_valida:
            if verificar_vitoria('O'):
                for linha in matriz:
                    print('Jogador O venceu!')
                    exit()
            break
        else:
            print('Jogada inválida!')
    
    while True: 
        for i in matriz:
            for l in i:
                print(l, end=' ')
            print()
        
        escolha = int(input('Escolha uma posição para X: '))
        jogada_valida = False
        
        for i in range(3):
            for l in range(3):
                if matriz[i][l] == escolha:
                    matriz[i][l] = 'X'
                    jogada_valida = True

        if jogada_valida:
            if verificar_vitoria('X'):
                for linha in matriz:
                    print('Jogador X venceu!')
                    exit()
            break
        else:
            print('Jogada inválida!')
    
    if all(type(item) == str for linha in matriz for item in linha):
        for linha in matriz:
            print(*linha)
        print('Empate!')
        break