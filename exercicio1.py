def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        print('digite um opção valida')
        x = int(input(pergunta))
    return x


while True:
    op =  valida_int('Incluir Nota do aluno? 0 - Não   1 - Sim ', 0, 1)
    if op == 0:
      break

    aluno = input('Nome do aluno: ')
    nota = float(input('Nota final: '))
    
    if 0 <= nota < 3:
        conceito = 'E'
    elif 3 <= nota < 5:
        conceito = 'D'
    elif 5 <= nota < 7:
        conceito = 'C'
    elif 7 <= nota < 9:
        conceito = 'B'
    elif 9 <= nota <= 10:
        conceito = 'A'
    else:
        print('Nota inválida.')
        break
    
    print('O aluno: {} tirou a nota: {} e se enquadra no conceito {}'.format(aluno, nota, conceito))
    
#função valida_int para validar os dados de entrarda.
#variavel op, decide se programa para ou continua no laço.
#variavel aluno amazena o nome do aluno.
#variavel nota amazena a nota do aluno.
# if é elif vai fazer as verificações necessárias.
# ex:
#nota maior ou igual a 0, é menor que 3 conceito = E
#nota maior ou igual a 3, é menor que 5 conceito = D
#else vai verificar se o usuario digitou uma nota diferente,
#ex:
#digitar um nota menor que 0 ou maior que 10 o programa sera encerrado! 