# Loop while (laço while)

tentativas = 0

while tentativas < 3:
    print('tente novamente')
    tentativas += 1

# Senha

senha = ''

while senha != '123456':
    senha = input('Digite sua senha')
print('Bem-vindo!')

# Receber nome do usuário

nome = ''

while nome == '':
    nome = input('Digite seu nome: ')
print(f'Bem-vindo {nome}')

# Ver por do sol as 17:00

horario = 0
while horario <= 17:
    print(horario)
    horario += 1
print('Hora de ver o por do sol')

# Contagem regressiva
contador = 100
while contador >= 0:
    print(contador)
    contador -= 1

# Desafio 1
# imprimir de 1 a 20
numero_inicial = 1
while numero_inicial <= 120:
    print(numero_inicial)
    numero_inicial += 1

# Desafio 2
# Entrar no programa se digitar a senha 'secreto'

senha = input('Digite sua senha: ')
while senha != 'secreto':
    senha = input('Digite sua senha novamente')
print('Seja bem-vindo')

# Desafio 3
# Imprimir numero decrescente de 100 para 1

numero1 = 100

while numero1 >= 1:
    print(numero1)
    numero1 -= 1
