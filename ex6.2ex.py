# crie um jogo de pedra, papel ou tesoura (jokenpo)
# voce devera jogar contra o computador.
# você irá sempre escolher um da opçoes
# .1-pedra, 2-papel, 3- tesoura
# .O computador irá sempre sortear um número
# de 1 até 3 para jogar
# .Armazene todos os resultados em uma lista e no final
# apresente o vencedor
# .Encerre o programa ao digeitar zero
import random

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def vencedor(jogador1, jogador2):
    global enpate, v1, v2
    if jogador1 == 1:
      if jogador2 == 1:
        enpate += 1
      elif jogador2 == 2:
        v2 += 1
      elif jogador2 == 3:
        v1 += 1

    elif jogador1 == 2:
      if jogador2 == 1:
        v1 += 1
      elif jogador2 == 2:
        enpate += 1
      elif jogador2 == 3:
        v2 += 1
    elif jogador1 == 3:
      if jogador2 == 1:
        v2 += 1
      elif jogador2 == 2:
        v1 += 1
      elif jogador2 == 3:
        enpate += 1
#Programa principal

print('JOKENPO')
print('1 - Predra')
print('2 - Papel')
print('3 - Tesoura')

resultados = []
jogadas = []
v1 = 0
v2 = 0
enpate = 0

while True:
    j1 = valida_int('Esconha sua jogada', 0, 3)
    if not j1:
        break
    j2 = random.randint(1,3)
    jogadas.append([j1, j2])
