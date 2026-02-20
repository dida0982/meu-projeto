#quanto de combustível se gastou na viagem ?

velocidade = float(input("Qual a velocidade do carro?"))
tempo = float(input("Quanto tempo durou a viagem?"))

distancia = tempo * velocidade
litros_usados = distancia/12

print("valocidade média:", velocidade, )
print("tempo gasto na viagem:", tempo)
print("distancia percorrida:", distancia)
print("quantidade de litros utilizada na viagem:", litros_usados)
