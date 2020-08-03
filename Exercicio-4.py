Preço_inicial=float(input("Digite o preço do produto: "))
Desconto=float(input("Digite a porcentagem de desconto a ser dada: "))
Valor_desconto=Preço_inicial*Desconto/100
Preço_final= Preço_inicial-Valor_desconto
print(f"O desconto será de R${Valor_desconto:.2f} e o preço final será de R${Preço_final:.2f}")
