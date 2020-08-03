animal1=float(input("Digite o peso do primeiro animal em kg: "))
animal2=float(input("Digite o peso do segundo animal em kg: "))
if animal1>animal2:
    print(f"O primeiro animal pesa {animal1}kg e o segundo {animal2}kg, portando o primeiro é mais pesado.")
elif animal1<animal2:
    print(f"O primeiro animal pesa {animal1}kg e o segundo {animal2}kg, portando o segundo é mais pesado.")
else:
    print(f"O primeiro animal pesa {animal1}kg e o segundo {animal2}kg, portando os dois possuem o mesmo peso.")
