lado1=float(input("Digite o tamanho do primeiro lado do triângulo"))
lado2=float(input("Digite o tamanho do segundo lado do triângulo"))
lado3=float(input("Digite o tamanho do terceiro lado do triângulo"))
if lado1+lado2>lado3 and lado2+lado3>lado1 and lado3+lado1>lado2:
    print("Parabéns!As medidas fornecidas configuram um triângulo.")
else:
    print("Infelizmente, as medidas fornecidas não configuram um triângulo.")
