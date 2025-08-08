year_now = int(input('Digite o ano que estamos: '))
year_born = int(input('Digite o ano em que nasceu: '))

age = year_now - year_born

print(f'A idade será de {age}')
print('\n')

# Exercicio Dolar

real = float(input('Digite a quantidade de reais que possui: '))
dolar = real/5.46

print(f'Você terá {dolar: .2f} dólares')
print('\n')

# Exercicio Temperatura

F = float(input('Digite a temperatura atual em fahrenhits: '))
C = (F - 32) / 1.8

print(f'Em graus será de {C: .2f}')
print('\n')

# Exercicio Preço

price = float(input('Digite o valor da compra: '))
imposto = (price * 60) / 100

print(f'O imposto será de {imposto: .2f}')
print('\n')

# Exercicio Empréstimo

emprestimo = float(input('Qual o valor desejado de empréstimo? '))
parcelaq = float(input('Qual a quantidade de parcela desejada? '))

juros = emprestimo * 1.20
parcelaf = juros / parcelaq

print(f'Você ira pagar {parcelaq: .2f} parcelas de {parcelaf: .2f} com os juros de 20% ja aplicados')