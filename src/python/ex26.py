print("Esse código vai calcular a raiz dos números")
print("")

# valor que será calculado
v = float(input("Digite um valor: "))

# qual raiz deseja (2 para quadrada, 3 para cúbica, 4 para quarta, etc.)
n = int(input("Digite qual raiz deseja (Ex: 2 para quadrada, 3 para cúbica, 4 para quarta): "))

# cálculo da raiz n-ésima
x = v ** (1/n)

print(f"A raiz {n}-ésima de {v} é {x:.4f}")
