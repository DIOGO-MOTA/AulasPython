#Desempacotamento de parâmetros em funcões

#def soma(*num):
 # soma = 0
 # print('Tupla: {}'.format(num))
 # for i in num:
#    soma += i
#  return soma

#print('Resultado: {}̣'.format(soma(1,2)))

#manipulando listas
 
mochila = ['Machado', 'Camisa']

mochila.append('Camisa')
print('lista:', mochila)

mochila.insert(1, 'Camisa')
print('lista:', mochila)

del mochila[1]
print('lista:', mochila)

mochila.remove('Camisa')
print('lista:', mochila)

#---------------------------------#
mochila = ['Machado', 'Camisa']

print(mochila[0][0]) #retona M
print(mochila[2][1]) #retona a

#---------------------------------
for item in mochila:
  for letra in item:
    print(letra, end='')
  print()
 # retona Machado Camisa

#---------------------------------