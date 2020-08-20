Salário=float(input("Digite o valor do seu salário: "))
Percentual=float(input("Digite a porcentagem do aumento: "))
Aumento=Salário*Percentual/100
Novo_salário=Aumento+Salário
print(f"Seu aumento foi de R${Aumento:.2f} e seu novo salário é de R${Novo_salário:.2f}")
