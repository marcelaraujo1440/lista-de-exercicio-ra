print("Escolha qual univerisdade deseja calcular a nota")
escolha= str(input("PUCPR\nUNICAMP\n: "))
if escolha=='PUCPR':
    ntp1= float(input('Insira a nota do seu 1 bimestre: '))
    ntp2= float(input("Insira a nota do seu 2 bimestre: "))
    ntp3= float(input("Insira a nota do seu 3 bimestre: "))
    ntp4= float(input("Insira a nota do seu 4 bimestre: "))
    mediapuc=(ntp1+ntp2+ntp3+ntp4)/4
    if mediapuc >= 7:
        print("Aprovado!")
    elif mediapuc < 7 and mediapuc >=4:
        print("Você está em exame")
    elif mediapuc < 4:
        print("Você reprovou!")
if escolha== "UNICAMP" :
    ntu1=float(input("Insira a sua nota do 1 bimestre: "))
    ntu2=float(input("Insira a sua nota do 2 bimestre: "))
    ntu3=float(input("Insira a sua nota do 3 bimestre: "))
    ntu4=float(input("Insira a sua nota do 4 bimestre: "))
    mediauni=(ntu1+ntu2+ntu3+ntu4)/4
    if mediauni>=5:
        print("Você foi aprovado")
    elif mediauni<5:
        print("Você ficou em exame")
    