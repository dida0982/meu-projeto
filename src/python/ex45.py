player = {
    "nome": "dida0982",
    "level": 1,
    "hp": 100,
    "exp": 0,
    "dano": 5,
}

npcs = [
    {"nome": "goblin", "hp": 30, "dano": 3, "exp": 10},
    {"nome": "troll", "hp": 50, "dano": 7, "exp": 20},
    {"nome": "dragão", "hp": 100, "dano": 15, "exp": 50},
    {"nome": "vampiro", "hp": 40, "dano": 5, "exp": 15},
]

print("Bem-vindo ao jogo de RPG!")
print(f"Você é {player['nome']} e está no nível {player['level']} com {player['hp']} HP.")
while True:
    print("\nO que você quer fazer?")
    print("1. Lutar contra um NPC")
    print("2. Ver status do jogador")
    print("3. Sair do jogo")
    
    escolha = input("Digite o número da sua escolha: ")
    
    if escolha == "1":
        npc = npcs[player["level"] - 1]
        print(f"\nVocê encontrou um {npc['nome']}!")
        
        while npc["hp"] > 0 and player["hp"] > 0:
            print(f"\n{npc['nome']} HP: {npc['hp']}")
            print(f"{player['nome']} HP: {player['hp']}")
            
            acao = input("Digite 'atacar' para atacar ou 'fugir' para fugir: ")
            
            if acao == "atacar":
                npc["hp"] -= player["dano"]
                print(f"Você atacou o {npc['nome']} e causou {player['dano']} de dano!")
                
                if npc["hp"] <= 0:
                    print(f"Você derrotou o {npc['nome']}!")
                    player["exp"] += npc["exp"]
                    print(f"Você ganhou {npc['exp']} de experiência!")
                    
                    if player["exp"] >= player["level"] * 20:
                        player["level"] += 1
                        player["hp"] += 20
                        player["dano"] += 2
                        print(f"Parabéns! Você subiu para o nível {player['level']}!")
                    break
                else:
                    player["hp"] -= npc["dano"]
                    print(f"O {npc['nome']} atacou você e causou {npc['dano']} de dano!")
                    
                    if player["hp"] <= 0:
                        print("Você foi derrotado! Fim de jogo.")
                        exit()
            elif acao == "fugir":
                print("Você fugiu do combate!")
                break
            else:
                print("Ação inválida. Tente novamente.")
                
    elif escolha == "2":
        print(f"\nStatus do jogador:")
        print(f"Nome: {player['nome']}")
        print(f"Nível: {player['level']}")
        print(f"HP: {player['hp']}")
        print(f"Experiência: {player['exp']}")
        print(f"Dano: {player['dano']}")
    elif escolha == "3":
        print("Obrigado por jogar! Até a próxima!")
        break
    else:
        print("Escolha inválida. Tente novamente.")

        print("Obrigado por jogar! Até a próxima!")
        break
    print("Escolha inválida. Tente novamente.")
    