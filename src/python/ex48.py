#codigo com função 

fluxo_caixa = []

print("-------------")
print("@ fluxo de caixa ")
print("-------------")
print("1 - adicionar valor")
print("2 - remover valor")
print("\n# Digite outro numero para encerrar #\n")

def adicionar_transacao():
    nome = input("nome: ")
    valor = float(input("valor: "))
    fluxo_caixa.append({"nome": nome, "valor": valor})

while True:

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        adicionar_transacao()
    elif opcao == 2:
        adicionar_transacao()
    else:
        break

    # nota fiscal
total = 0
for fc in fluxo_caixa:
    print("Nome:", fc['nome'], "Valor: R$", fc['valor'])
    total += fc['valor']

print("Saldo total: R$", total)