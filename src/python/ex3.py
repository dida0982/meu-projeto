valor = input("Digite um valor: ")

# Booleano
if valor.lower() == "true" or valor.lower() == "false":
    print("É booleano")

# Inteiro
elif valor.isdigit() or (valor.startswith("-") and valor[1:].isdigit()):
    print("É inteiro")

# Real (float)
elif valor.replace(".", "", 1).isdigit() or (
    valor.startswith("-") and valor[1:].replace(".", "", 1).isdigit()
):
    print("É número real")

# Caractere
elif len(valor) == 1:
    print("É caractere")

# Cadeia
else:
    print("É cadeia (string)")

