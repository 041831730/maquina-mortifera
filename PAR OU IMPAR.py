
numero = int(input('Me diga um numero qualquer: '))
resultado = numero % 2 # o simbolo de % so aparece dois resultados 0 e 1
if resultado == 0: # se o numero for verdadeiro igual 0 e par
    print('O numero {} e par'.format(numero))
else: # se o numero for falso igual a 1 e impar
    print('o numero {} é impar'.format(numero))