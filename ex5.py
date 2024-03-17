h= float(input('Qual sua altura em Metros? '))
genero= input('Qual o seu gênero?\n1-Homem\n2-Mulher\nDigite qual o seu gênero: ')
homem=(72.7*h)-58
mulher=(62.1*h)-44.7 
if int(genero)==1:
    print(f'O peso ideal de um homem com {h} de altura é de {homem: .2f} Kg')
else: 
    print(f'O peso ideal de uma mulher com {h} de altura é de {mulher: .2f} Kg')

   