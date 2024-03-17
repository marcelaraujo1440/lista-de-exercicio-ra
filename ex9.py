#Entrada de dados
nome= input("Qual seu nome? ")
idade= int(input("Qual sua idade? "))
tempo= int(input("Quanto tempo o senhor está atuando no mercado de trabalho? "))
tnm= tempo-idade
if tempo>=25 and idade>=60 or idade>=65 or tempo>+30:
    print('O senhor já pode se aposentar!')
else:
    print('Você ainda nao pode se aposentar')