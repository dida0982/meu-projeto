print("Este código vai fazer o cálculo da velocidade de um projétil. ")

distancia = float(input("Quantos metros o projétil percorreu? "))
tempo = float(input("Quantos segundos ele demorou?"))

velocidade = (distancia * 1000 / tempo * 60)

print(f"O projétil se deslocou a uma velocidade de {distancia}/{tempo}")
