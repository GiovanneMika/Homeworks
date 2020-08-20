nota1=float(input("Digite o valor da sua primeira nota: "))
nota2=float(input("Digite o valor da sua segunda nota: "))
media=(nota1+nota2)/2
if media>10:
    print(f"O valor máximo de média é 10, portanto uma média {media:.1f} é inválida.")
elif media>=7:
    print(f"A sua média é {media:.1f}, portanto você não necessita de recuperação.")
else:
    print(f"A sua média é {media:.1f}, portanto será necessário a permanência para a recuperação.")
