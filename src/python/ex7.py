#quanto de combustível se gastou na viagem ?

velocidade = float(input("Qual a velocidade do carro?"))
tempo = float(input("Quanto tempo durou a viagem?"))

distancia = tempo * velocidade
litros_usados = distancia/10

print(f"valocidade média: {velocidade:.2f} ")
print(f"tempo gasto na viagem: {tempo:.2f}")
print(f"distancia percorrida: {distancia:.2f}")
print(f"quantidade de litros utilizada na viagem: {litros_usados:.2f}")
