lado1=float(input("Digite o tamanho do primeiro lado do triângulo"))
lado2=float(input("Digite o tamanho do segundo lado do triângulo"))
lado3=float(input("Digite o tamanho do terceiro lado do triângulo"))
if lado1+lado2<lado3 or lado2+lado3<lado1 or lado3+lado1<lado2:
    print("As medidas dos lados informados não configuram um triângulo")
elif lado1==lado2 and lado1==lado3:
        print("As medidas dos lados informados configuram um triângulo equilátero")
elif lado1!=lado2 and lado1!=lado3 and lado2!=lado3:
            print("As medidas dos lados informados configuram um triângulo escaleno")
else:
    if lado1==lado2 and lado2!=lado3 or lado2==lado3 and lado2!=lado1 or lado1==lado3 and lado1!=lado2:
                print("As medidas dos lados informados configuram um triângulo isósceles")
