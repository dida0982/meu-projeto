print("Este código vai fazer o cálculo da velocidade de um projétil que percorre uma distância em km em um espaço de tempo em minutos. Vai ser apresentado em metros por segundo. ")

distancia = float(input("Quantos metros o projétil percorreu? "))
tempo = float(input("Quantos segundos ele demorou?"))

velocidade = (distancia * 1000 / tempo * 60)
