print("Este código vai fazer o cálculo da velocidade de um motoqueiro. ")

distancia = float(input("Quantos km o motoqueiro percorreu? "))
tempo = float(input("Quantos minutos ele demorou?"))

velocidade = (distancia*1000)/(tempo*60)

print(f"O motoqueiro se deslocou a uma velocidade de: {velocidade:.0f}m/s")
