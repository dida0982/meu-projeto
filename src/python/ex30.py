# Listas para armazenar os dados
nomes = []
idades = []
alturas = []

# Primeiro laço: coletar os dados
for i in range(3):  # de 1 até 3 (mas em Python começa no 0)
    nome = input(f"Digite o nome da pessoa {i+1}: ")
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    altura = float(input(f"Digite a altura da pessoa {i+1}: "))

    nomes.append(nome)
    idades.append(idade)
    alturas.append(altura)

print("\n--- Dados coletados ---")

# Segundo laço: mostrar os dados
for i in range(3):
    print(f"Pessoa {i+1}: Nome = {nomes[i]}, Idade = {idades[i]}, Altura = {alturas[i]}")
