sm = int(input("Salário mensal: "))
pr = int(input("pecentual de reajuste: "))

ns = sm*(1+0.10)

print(f"O novo salário com o 10% de ajuste: {ns:.2f}")
