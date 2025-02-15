# COntinue, ignorar/pular
# função para inprimir numeros pares
""" for numero in range(100):
    if numero % 2 == 0:
        print(numero)
    else:
        continue """

""" for numero in range(100):
    if numero % 2 == 0:
        print(numero)
    else:
        break """

""" frutas = ['Maça', 'Manga', 'Laranja', 'Morango']
for fruta in frutas:
    if fruta == 'Manga':
        continue
    print(f'{fruta} adicionada a dieta') """

# Desafio 1
estilos = ['Hip-hop', 'Rock', 'Rap', 'Pop']
for estilo in estilos:
    if estilo == 'Rap':
        continue
    print(f'Você está ouvindo {estilo} ')


print('---------------------')
# Desafio 2

estilos = ['Hip-hop', 'Rock', 'Rap', 'Pop']
for estilo in estilos:
    if estilo == 'Rap':
        break
    print(f'Você está ouvindo {estilo} ')
