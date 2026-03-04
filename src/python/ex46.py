import os 

mensagens = []

nome = input("Digite seu nome: ")

while True:

    #limpando terminal
    os.system('cls')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])

    print("_________________")

    #obtendo texto
    texto = input("Digite uma mensagem: ")
    if texto == "fim":
        break

    #adicionando mensagem
    mensagens.append({
        "nome": nome,
        "texto": texto
    })