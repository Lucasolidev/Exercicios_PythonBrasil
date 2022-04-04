""" 11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo."""

num1 = int(input('Digite o primeiro numero inteiro: '))
num2 = int(input('Digite o segundo numero inteiro: '))
num3 = float(input('Digite um numero real: '))

calc1 = (2 * num1) * (num3/2)
calc2 = (num1 * 3) + num3
calc3 = num3 ** 3

print(f'O calculo do produto do dobro do primeiro com metade do segundo e: {calc1}')
print(f'A soma do triplo do primeiro com o terceiro: {calc2}')
print(f'O terceiro elevado ao cubo: {calc3}')
