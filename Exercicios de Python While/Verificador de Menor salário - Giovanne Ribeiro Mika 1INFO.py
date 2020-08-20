c=0
menors=float(input("Digite o valor do salário: "))
while(c<14):
    s=float(input("Digite o valor do salário: "))
    c+=1
    if menors>s:
        menors=s
print(f"O menor salário foi de R${menors:.2f}.")
