import random

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        print('digite um opção valida')
        x = int(input(pergunta))
    return x

def cadastra(nome, valor, ru):
    listaSorteio.extend( ((nome + ru[-2::] + ' ' ) * int(valor//10)).split()) 
    return

def sorteio():
    random.shuffle(listaSorteio)
    print('Lista sorteio: {}'.format(listaSorteio))
    return random.choice(listaSorteio)

listaSorteio = []

while True:
    op =  valida_int('Cadastrar um doador ? 0 - Não   1 - Sim ', 0, 1)
    if op == 0:
      break

    doador = input('Nome do doador: ')
    valor = float(input('Valor da doação: '))
    if valor < 10:
      print('Valor mínimo para doação é de R$ 10 !')
      continue
    ru = input('Digite sua RU: ')
    
    cadastra(doador, valor, ru)
    
if len(listaSorteio) > 0:
  print('Lista de doadores: {}'.format(listaSorteio))    
  print('O vencedor(a) foi: {}'.format(sorteio()))
else:
  print('Programa finalizado...')


#função valida_int para validar os dados de entrarda.
#variavel op, decide se programa para ou continua no laço.

