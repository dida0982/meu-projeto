notas = []

contador = 0
while contador < 5:
    codigo_aluno = input("Digite o código do aluno: ")
    nota_aluno = float(input("Digite a nota do aluno: "))
    resultado = [codigo_aluno, nota_aluno]
    notas.append(resultado)
    contador += 1

print(f"\nTotal de alunos cadastrados: {len(notas)}")

for aluno in notas:
    print(f"Aluno: {aluno[0]}, Nota: {aluno[1]}")