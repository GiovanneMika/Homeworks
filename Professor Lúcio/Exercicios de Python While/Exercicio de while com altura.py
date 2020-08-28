c=0
altme=0
altma=0
altmeio=0
while(c<5):
    alt=float(input("Digite a sua altura, em cm: "))
    c+=1
    if alt>180:
        altma+=1
    if alt<160:
        altme+=1
    if alt>160 and alt<180:
        altmeio+=1
print(f"Das {c} alturas informadas, {altma} são maiores que 180cm e {altme} são menores que 160cm. {altmeio} estão entre 180 e 160.")


