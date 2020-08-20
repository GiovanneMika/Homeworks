c=0
s=0
maiors=0
menors=float(input("Digite o valor do salário: "))
while(c<4):
    s=float(input("Digite o valor do salário: "))
    c+=1
    if maiors<s:
        maiors=s
    if menors>s:
        menors=s
print(f"O maior salário foi de R${maiors:.2f} e o menor foi de R${menors:.2f}")
