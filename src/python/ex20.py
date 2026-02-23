print(" ")
print("Este código vai fazer o cálculo de um reajuste salarial.")
print(" ")

sm = int(input("Qual o salário mensal: "))
pr = int(input("Qual o percentual do reajuste? (Ex: se for 10 porcento coloca 1.10, se for 20 porcento coloca 1.20, se for de 5 porcento coloca 1.05 etc...): "))

ns = sm*(pr)

print(f"O novo salário com o 10% de ajuste: {ns:.2f}")
