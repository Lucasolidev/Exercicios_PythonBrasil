# 7 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
quadrado = float(input('Digite a area de um quadrado: '))

area = (quadrado * quadrado) * quadrado
print(f'A area do quadrado em dobro: {area:.2f}')
