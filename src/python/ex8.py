valor = float(input("Qual o valor do produto?"))
taxa = float(input("Quanto é a taxa?"))
tempo = float(input("Qual o tempo?"))


prestacao = valor + (valor*(taxa/100)*tempo)

print(f"pretação de: {prestacao:.2f}")
