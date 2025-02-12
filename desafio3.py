""" 
A velocidade maxima para essa rua é 50km
*Cruzou entre 51km e 60km, levou multa de 2 pontos
*Cruzou entre 61km e 75km, levou multa de 3 pontos
*Cruzou acima de 75km, levou multa de 7 pontos
 """
velocidade_atual = int(input('Qual sua velocidade? '))

if velocidade_atual <= 50:
    print('Você não será multado!')
elif velocidade_atual >= 51 and velocidade_atual <= 60:
    print('Você levou multa de 2 pontos')
elif velocidade_atual >= 61 and velocidade_atual <= 75:
    print('Você levou multa de 3 pontos')
else:
    print('Você foi multado em 7 pontos')
