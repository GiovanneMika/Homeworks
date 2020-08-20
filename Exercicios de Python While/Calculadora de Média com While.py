c=0
s=0
while(c<10):
    p=float(input("Digite o preço: "))
    s=s+p
    c=c+1
media=s/c
print(f"A soma total dos preços foi R${s:.2f}, com uma média de R${media:.2f}.")
