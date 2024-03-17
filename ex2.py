a= float(input('Digite um valor: '))
b=float(input('Digite o segundo valor: '))
c= float(input('Digite o terceiro valor: '))
delta= b**2-4*b*c
if delta=='0':
    print('existem duas raízes reais iguais')
elif delta>0:
    print('existem duas raízes imaginárias conjugadas')
elif delta<0:
    print('existem duas raízes reais distintas')
