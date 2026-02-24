#Lista de tres pessoas com idade e altura de cada uma.

nomes = []
idades = []
alturas = []

for i in range(3):
    nome = input(f"Digite um nome {i+1}: ")
    idade = int(input(f"Digite a idade {i+1}: "))
    altura = float(input(f"Digite a altura {i+1}: "))

nomes.append(nome)
idades.append(idade)
alturas.append(altura)

print("")

for i in range(3):
    print(f"Pessoa {i+1}: Nome = {nomes[i]}, Idade = {idades[i]}, Altura = {alturas[i]}")
