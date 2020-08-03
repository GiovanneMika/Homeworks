Dias=int(input("Digite o numero de dias que o carro ficou alugado: "))
Quilometragem=float(input("Digite a quilometragem percorrida: "))
Aluguel= Dias*50.00+Quilometragem*0.40
print(f"O valor total do aluguel é de R${Aluguel:.2f}")
c=input("Digite <enter> para sair")
