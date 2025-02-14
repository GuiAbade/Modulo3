""" # Loop Aninhados
# País + Estação

paises = ['brasil', 'india', 'estados unidos']
estacoes_do_ano = ['primavera', 'verao', 'outono', 'inverno']
for pais in paises:
    for estacao in estacoes_do_ano:
        print(f'{pais} {estacao}')

for x in range(1, 11):
    for y in range(1, 6):
        print(f'Valor externo {x} e interno {y}')
 """

# Desafio:

celulares = ['Asus', 'Samsung', 'Sony', 'IPhone']
versoes = ['Plus', 'Premium Plus', 'Premium Deluxe', 'Plus Premium Ultra']

for celular in celulares:
    for versao in versoes:
        print(f'{celular} e o modelo é {versao}')
