velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade >=80:
    print('MULTADO! Você Excedeu o Limite Permitido e de 80Km/h')
    multa = (velocidade-80) * 7
    print('voce deve pagar a multa de R${}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')