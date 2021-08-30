# Imagine uma situaçao na qual voce deve realizar
# cadastro de uma lista de compras em um sistema.
# Cada produto comprado deverá ser registrado com 
# seu nome,quantidade e valor unitário

mercado = []

for i in range(3):
 nome = input('Digite o nome do item:')
 qts = int(input('Digite a quantidade:'))
 valor = float(input('Digite o valor:'))
 mercado.append([nome, qts, valor])
print(mercado)

soma = 0
print('Lista de compras:')
print('-' * 20)
print('item | quantidade | valor unitário | total do item')
for item in mercado:
  print('{} | {} | {} | {} '.format(item[0], item[1], item[2], item[1] * item[2]))
  soma += item[1] * item[2]
print('-' * 20)
print('Total a ser pago: {}'.format(soma)) 