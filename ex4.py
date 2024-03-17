b1= int(input('Qual foi a sua nota no 1 bimestre? ' ))
b2= int(input('Qual foi a sua nota no 2 bimestre? ' ))
b3= int(input('Qual foi a sua nota do 3 bimestre? ' ))
b4= int(input('Qual foi a sua nota no 4 bimestre? ' ))
media= ((b1+b2+b3+b4)/4)
print(f"{media}")
if media >= 7:
    print("Estudante aprovado!")
elif media>= 4 and media <7:
    print("Estudante em recuperação!")
elif media<4:
    print('Estudante reprovado!') 
else:
    print('Error')