idade=int(input("Digite a sua idade:"))
if idade<16:
    print(f"Você possui {idade} anos, portanto não tem a idade necessária e não pode fazer um título de eleitor.")
else:
    if idade>=70:
        print(f"Você possui {idade} anos, portanto o seu voto não é obrigatório, assim como seu título de eleitor.")
    else:
        print(f"Você possui {idade} anos, portanto tem a idade necessária e pode fazer um título de eleitor.")

