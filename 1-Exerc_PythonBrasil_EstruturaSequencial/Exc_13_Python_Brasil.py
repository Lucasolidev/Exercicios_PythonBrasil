""" 13 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7"""

altura = float(input('Qual sua altura? '))

peso_ideal_h = (72.7 * altura) - 58
peso_ideal_m = (62.1 * altura) - 44.7

print(f'Seu peso ideal para homens e: {peso_ideal_h:.2f} KG')
print(f'Seu peso ideal para mulheres e: {peso_ideal_m:.2f} KG')
