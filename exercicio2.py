def cria_email(nome, sobrenome, ru):
 x = nome[0] + sobrenome + ru[-2::] + '@algoritmos.com.br'
 return x

print(cria_email('diogo', 'mota', '3766232'))