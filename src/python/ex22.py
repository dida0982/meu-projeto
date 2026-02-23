print("Este código vai fazer o cálculo da velocidade de um projétil. ")

distancia = float(input("Quantos km o projétil percorreu? "))
tempo = float(input("Quantos minutos ele demorou?"))

velocidade = (distancia*1000)/(tempo*60)

print(f"O projétil se deslocou a uma velocidade de: {distancia:.0f}{tempo:.0f}m/s")
