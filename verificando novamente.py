#divida seu programa em pequenos pedaços, usuario e pior raça que tem vai fazer algo para travar
frase = str(input('digite um frase: ')).upper().strip()
#strip remove os espaços
print('loanding...')
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}°'.format(frase.find('A') +1))
#find procure a partir do lado esquerdo 
print('a ultima ocorrencia de A apareceu na posiçao {}°'.format(frase.rfind('A') +1))
# rfind procure a partir do lado direito
