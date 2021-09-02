def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def cria_email(nome, sobrenome, ru):
    x = nome[0] + sobrenome + ru[-2::] + '@algoritmos.com.br'
    print('Sr.ª  {} {}, seu email é {}'.format(nome, sobrenome, x))
    return 


while True:
    op =  valida_int('Criar um email ? 0 - Não   1 - Sim ', 0, 1)
    if op == 0:
      break
    
    nome =  input('Digite seu nome: ') 
    sobrenome = input('Digite seu sobrenome: ')
    ru = input('Digite sua RU: ')

    cria_email(nome, sobrenome, ru)


# Função valida_int para validar os dados de entrarda.
# Variavel op, decide se programa para ou continua no laço.
# Variavel nome amazena o nome.
# variavel sobrenome amazena o sobrenome.
# variavel ru amazena o ru.
# Função cria_email vai receber como parametro o nome, sobrenome, ru
# Dentro da função cria_email foi criada um variavel X, para amarzenar 
# o valor do nome e sobrenome e os dois últimos digitos do seu ru mais 
# a string '@algoritmos.com.br' concatenado.
# print dentro da função  para imprimir o resultado.

