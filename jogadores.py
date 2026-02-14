# Debate de Craques - Comparador de Jogadores
# Base de dados de jogadores

jogadores = {
    "neymar": {
        "nome": "Neymar Jr",
        "qualidade": 9.5,
        "carreira": 9.0,
        "relevancia": 9.5,
        "nacionalidade": "🇧🇷"
    },
    "messi": {
        "nome": "Lionel Messi",
        "qualidade": 10,
        "carreira": 10,
        "relevancia": 10,
        "nacionalidade": "🇦🇷"
    },
    "ronaldo": {
        "nome": "Cristiano Ronaldo",
        "qualidade": 9.5,
        "carreira": 10,
        "relevancia": 10,
        "nacionalidade": "🇵🇹"
    },
    "kdb": {
        "nome": "Kevin De Bruyne",
        "qualidade": 9.0,
        "carreira": 7.5,
        "relevancia": 8.0,
        "nacionalidade": "🇧🇪"
    },
    "mbappe": {
        "nome": "Kylian Mbappé",
        "qualidade": 9.5,
        "carreira": 8.5,
        "relevancia": 9.5,
        "nacionalidade": "🇫🇷"
    },
    "haaland": {
        "nome": "Erling Haaland",
        "qualidade": 9.0,
        "carreira": 8.0,
        "relevancia": 9.0,
        "nacionalidade": "🇳🇴"
    }
}

def comparar_jogadores(jogador1, jogador2):
    """Compara dois jogadores e dá o veredicto"""
    
    j1 = jogadores.get(jogador1.lower())
    j2 = jogadores.get(jogador2.lower())
    
    if not j1 or not j2:
        return "Jogador não encontrado na base de dados!"
    
    print(f"\n⚽ {j1['nome']} {j1['nacionalidade']} vs {j2['nome']} {j2['nacionalidade']}\n")
    print("=" * 50)
    
    # Calcular diferenças
    diff_qualidade = j1['qualidade'] - j2['qualidade']
    diff_carreira = j1['carreira'] - j2['carreira']
    diff_relevancia = j1['relevancia'] - j2['relevancia']
    
    # Mostrar comparação
    print(f"📊 QUALIDADE:    {j1['qualidade']:.1f} vs {j2['qualidade']:.1f} → {veredito_criterio(diff_qualidade)}")
    print(f"🏆 CARREIRA:     {j1['carreira']:.1f} vs {j2['carreira']:.1f} → {veredito_criterio(diff_carreira)}")
    print(f"🌟 RELEVÂNCIA:   {j1['relevancia']:.1f} vs {j2['relevancia']:.1f} → {veredito_criterio(diff_relevancia)}")
    
    # Média geral
    media_j1 = (j1['qualidade'] + j1['carreira'] + j1['relevancia']) / 3
    media_j2 = (j2['qualidade'] + j2['carreira'] + j2['relevancia']) / 3
    diferenca = media_j1 - media_j2
    
    print("\n" + "=" * 50)
    print(f"📈 MÉDIA GERAL: {media_j1:.2f} vs {media_j2:.2f}")
    print(f"\n🎯 VEREDICTO FINAL: {j1['nome']} é {veredito_final(diferenca)}")
    print("=" * 50)

def veredito_criterio(diferenca):
    """Retorna o veredito para cada critério"""
    if diferenca >= 1.5:
        return "MUITO MELHOR ✅✅"
    elif diferenca >= 0.5:
        return "MELHOR ✅"
    elif diferenca <= -1.5:
        return "MUITO PIOR ❌❌"
    elif diferenca <= -0.5:
        return "PIOR ❌"
    else:
        return "EQUIPARADO ⚖️"

def veredito_final(diferenca):
    """Retorna o veredicto final"""
    if diferenca >= 1.5:
        return "MUITO MELHOR! 🔥🔥🔥"
    elif diferenca >= 0.5:
        return "MELHOR! 🔥"
    elif diferenca <= -1.5:
        return "MUITO PIOR! 💀💀"
    elif diferenca <= -0.5:
        return "PIOR! 💀"
    else:
        return "EQUIPARADO! ⚖️"

def listar_jogadores():
    """Lista todos os jogadores disponíveis"""
    print("\n⚽ JOGADORES DISPONÍVEIS:\n")
    for key, value in jogadores.items():
        print(f"  • {value['nome']} {value['nacionalidade']} (digite: {key})")
    print()

# Menu principal
def main():
    print("\n" + "=" * 50)
    print("⚽ BEM-VINDO AO DEBATE DE CRAQUES! ⚽")
    print("=" * 50)
    
    while True:
        print("\nO que queres fazer?")
        print("1 - Comparar 2 jogadores")
        print("2 - Ver jogadores disponíveis")
        print("3 - Sair")
        
        escolha = input("\nEscolhe (1/2/3): ")
        
        if escolha == "1":
            listar_jogadores()
            j1 = input("Jogador 1: ")
            j2 = input("Jogador 2: ")
            comparar_jogadores(j1, j2)
            
        elif escolha == "2":
            listar_jogadores()
            
        elif escolha == "3":
            print("\n👋 Até logo, craque!\n")
            break
        else:
            print("❌ Opção inválida!")

if __name__ == "__main__":
    main()
