# 9 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

fahr = float(input('Digite o valor da temperatura em Fahrenheit: '))

fahr_celsius_1 = ((fahr-32)/1.8)  # formula opção 1
fahr_celsius_2 = 5 * ((fahr-32) / 9)  # formula opção 2

print(f'A temperatura em celsius e: {fahr_celsius_1}C')
print(f'A temperatura em celsius e: {fahr_celsius_2}C')
