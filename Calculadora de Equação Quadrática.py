import math
A=float(input("Digite o valor do coeficiente A: "))
B=float(input("Digite o valor do coeficiente B: "))
C=float(input("Digite o valor do coeficiente C: "))
Delta=B**2-4*A*C
if Delta<0:
    print(f"Seu delta vale {Delta} , portanto a equação não possui raízes reais.")
if (Delta >=0):
    x1=(-B+math.sqrt(Delta))/(2*A)
    x2=(-B-math.sqrt(Delta))/(2*A)
if (Delta>0):
    print(f"Seu delta vale {Delta} , portanto a equação possui 2 raízes {x1} e {x2} reais e distintas.")
elif (Delta==0):
    print(f"Seu delta vale {Delta} , portanto a equação possui raízes {x1} e {x2} reais iguais.")
