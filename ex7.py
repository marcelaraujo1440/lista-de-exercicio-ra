nome= input('Qual seu nome? ')
idade= int(input('Qual a sua idade? '))
peso= float(input('Qual o seu peso em Kg?'))
if idade> 15:
    print('Está liberado para ir ao parque!')
elif idade<15:
    print('Ainda não é permitida a entrada com a sua idade!')
if peso<120:
    print('Está lliberado para ir ao parque!')
elif peso>120: 
    print('O senhor está obeso, se retire daqui!')