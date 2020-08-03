salario=float(input("Digite seu salário:"))
if salario<=1500:
    valor_desconto=salario*0.08
    print(f"O valor que será descontado pelo INSS em seu salário será de R${valor_desconto:.2f}")
else:
    if salario<=2500:
        valor_desconto=salario*0.09
        print(f"O valor que será descontado pelo INSS em seu salário será de R${valor_desconto:.2f}")
    else:
        if salario<= 3500:
            valor_desconto=salario*0.1
            print(f"O valor que será descontado pelo INSS em seu salário será de R${valor_desconto:.2f}")
        else:
            if salario>3500:
                valor_desconto=salario*0.14
                print(f"O valor que será descontado pelo INSS em seu salário será de R${valor_desconto:.2f}")

