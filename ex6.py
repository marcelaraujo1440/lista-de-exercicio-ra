impar=0
par=0
numero = int(input("Informe um número: "))
if numero % 2 == 0:
    print("Esse número é par")
    par+=1
else:
    print('Esse numero é impar')
    impar+=1
print(f'Par:{par}\nImpar:{impar}')