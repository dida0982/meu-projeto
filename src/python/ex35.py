n = 5

while True:
    x = int(input("Digite um valor de 1 a 10: "))

    if x == n:
        print(f"Você encontrou o valor de x: {x}")
        break  # encerra o loop quando acertar
    elif x < n:
        print(f"{x} Seu valor é baixo")
    elif x > n:
        print(f"{x} Seu valor é alto")
    else:
        print("Você não achou o número. Tente de novo")
