"""17 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a 
ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é 
vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre
arredonde os valores para cima, isto é, considere latas cheias."""

import math
#math.ceil arredonda para cima o valor

area_pintada = 100 #float(input('Qual valor metros da area a ser pintada? ')) 
area_folga = area_pintada * 1.1
litros_por_metro = 6
litros_ser_usados = area_folga / litros_por_metro

litros_por_latas = 18
litros_usados_latas = math.ceil(litros_ser_usados / litros_por_latas)
valor_latas = litros_usados_latas * 80
print(f'Quantidade de latas 18Lt a ser comprada: {litros_usados_latas:.0f} no valor de R$ {valor_latas:.2f}')

litros_metros_galoes = 3.6
litros_usados_galoes = math.ceil(litros_ser_usados / litros_metros_galoes)
valor_galoes = litros_usados_galoes * 25
print(f'Quantidade de galoes 3.6Lt a ser comprada: {litros_usados_galoes:.0f} no valor de R$ {valor_galoes:.2f}')

# compra de tinta otimizada por valor

litros_usados_latas = math.floor(litros_ser_usados / litros_por_latas)
valor_latas = litros_usados_latas * 80
litros_faltantes = litros_ser_usados % litros_por_latas
litros_usados_galoes = math.ceil(litros_faltantes / litros_metros_galoes)
valor_galoes = litros_usados_galoes * 25
valor_total = valor_latas + valor_galoes
print(f'Voce deverar usar {litros_usados_latas:.0f} latas de 18 litros mais {litros_usados_galoes} galoes de 3.6 litros, no valor de R$ {valor_total:.2f}')