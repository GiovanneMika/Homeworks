c=0
menorp=float(input("Digite o peso do animal: "))
somap=menorp
maiorp=menorp
while(c<19):
    p=float(input("Digite o peso do animal: "))
    c+=1
    somap+=p
    if maiorp<p:
        maiorp=p
    if menorp>p:
        menorp=p
mediap=somap/(c+1)
print(f"A média dos pesos é {mediap}kg, com o maior peso sendo de {maiorp}kg e o menor sendo de {menorp}kg.")
