c=0
sn=0
man=0
men=11
me6=0
while(c<10):
    n=float(input("Digite a sua nota: "))
    c+=1
    sn+=n
    if man<n:
        man=n
    if men>n:
        men=n
    if n<6:
        me6+=1
media=sn/c
print(f"A média das notas é {media}, a maior nota é {man} e a menor é {men}, com {me6} notas abaixo de 6.")