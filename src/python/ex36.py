
sa = float(input("Digite o valor do salário: "))

if sa<500:
    ns=sa*1.15
    print(f"Acrescimo de 15%")
elif sa <= 1000:
    ns=sa*1.10
    print(f"Acrescimo de 10%")
else:
    ns=sa*1.15
    print(f"Acrescimo de 15%.")

print(f"Novo sário: {ns:.2f}")
