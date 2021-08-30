# Dada um lista contendo as notas de alunos 
# em uma disciplina, escreva uma expressão para: 
# notas = [9,7,7,10,3,9,6,6,2] 
# a) Encontrar quantos alunos tiraram nota 7 
# b) Encontar a Maior nota
# c) Ordernar a lista de Notas 
# d) A média das notas

notas = [9,7,7,10,3,9,6,6,2] 

# a) print(notas.count(7))

# b)
maiorNota = max(notas)
print(maiorNota)

# c)
orden = sorted(notas)
print(orden)

# d)
soma = 0
tam = len(notas)
for nota in notas:
  soma += nota

  media = soma / tam
  
print(media)