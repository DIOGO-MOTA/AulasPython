def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        print('digite um opção valida')
        x = int(input(pergunta))
    return x

def cadastra(produto):
    lista.append(produto)
    return

lista = []

while True:
    op =  valida_int('Cadastrar novo produto ? 0 - Não   1 - Sim ', 0, 1)
    if op == 0:
      break

    produtos = {}

    produtos['codigo'] = int(input('Digite o código: '))
    
    if produtos['codigo'] == 0:
        print('Digite um código valido.')
        break
    
    produtos['estoque'] = int(input('Digite a quantidade em estoque: '))
    produtos['minimo'] = int(input('Digite a quantidade mínima do estoque: '))
    
    cadastra(produtos)
    

listaOrdenada = sorted(lista, key=lambda item: item['codigo'])
print(listaOrdenada)


 