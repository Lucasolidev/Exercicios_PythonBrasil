# 8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganho_hora = float(input('Quanto voce ganha por hora?: '))
hora_mes = float(input('Quantas horas trabalhada no mes?: '))

calc = ganho_hora * hora_mes

print(f'Seu salario total do mes sera de: R${calc:.2f} reais')
