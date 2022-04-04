"""18 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de 
Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)."""

tamanho_arquivo = float(input('Qual o tamanho do arquivo em MB? '))
velocidade_link = float(input('Qual a velocidade da internet em Mbps? '))

segundos = tamanho_arquivo/velocidade_link
minutos = int(segundos/60)
print(minutos)
segundos = segundos % 60
print(segundos)
print(f"Tempo aproximado para download: {minutos} minutos e {segundos:.2f} segundos")