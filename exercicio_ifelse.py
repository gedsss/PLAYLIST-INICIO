# Exercicio de carteira de motorista

ano_atual = int(input('Digite o ano atual: '))
data_nasciment = int(input('Digite a sua data de nascimento: '))

idade = ano_atual - data_nasciment

if idade < 18:
  print('Voce não está apto a tirar a carteira de motorista!')
else:
  print('Voce está apto a tirar a carteira de motorista')
print('\n')

# Exercicio de media de aluno 

n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))

nf = (n1 + n2) / 2

if (nf >= 7):
  print('Aluno aprovado!')
else:
    if (nf >= 5) and (nf < 7):
        print('Aluno reprovado!')
    else:
       print('Aluno reprovado')
print('\n')

# Exercicio de massa corporal

massa = float(input('Digite a sua massa: '))
altura = float(input('Digite a sua altura: '))
imc = massa / altura / (altura ** 2)

if imc < 17:
    print('muito abaixo do peso')
elif (imc >= 17) and (imc <= 18.5):
    print('Abaixo do peso')
elif (imc >= 18.5) and (imc < 25):
    print('Peso ideal')
elif (imc >= 25) and (imc < 30):
    print('Sobrepeso')
elif (imc >= 30) and (imc < 35):
    print('Obesidade')
elif (imc >= 35) and (imc < 40):
    print('Obesidade severa')
else:
   print('Obesidade mórbida')
print('\n')

# Exercicio times

santos = float(input('Digite quantos gols o maior time do mundo fez: '))
corinthians = float(input('Digite quantos gols o menor time de São Paulo fez: '))

dif = 0

if santos > corinthians:
   dif = santos - corinthians
elif corinthians > santos:
   dif = corinthians - santos

if dif == 0:
   print('Empate!')
elif (dif > 0) and (dif <= 3):
   print('Partida comum!')
elif dif > 3:
   print('Goleada!')
