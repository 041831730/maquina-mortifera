n = str(input('digite seu nome completo: ')).strip()
nome = n.split()
#split pega nome inteiro e dividi em pedaços separados por espaço
print('Muito Prazer Em Te Conhecer')
print('Seu Primeiro nome é {}'.format(nome[0]))
print('seu ultimo nome é {}'.format(nome[len(nome)-1]))
#len significa quantas posiçoes tem nome
#-1 porque yuta freitas de lima tem 3 ele vai de 0 ate 2