def mostrar_tabuleiro(tabuleiro):
    # O tabuleiro tem 3 linhas, para cada uma...
    for i in range(3):
        # Mostra a primeira célula, uma barra, e mesmo com a segunda e terceira
        print(f"{tabuleiro[i][0]}|{tabuleiro[i][1]}|{tabuleiro[i][2]}")

def posicao_livre(linha, coluna, tabuleiro):
    # Se o valor da casa for "___", ela está livre
    if tabuleiro [linha][coluna] == '___':
        return True
    else:
        return False

def jogar(jogador, tabuleiro):
    # Pede ao jogador uma entrada
    while True: # Loop só para se a jogada for válida
        print(f"É a vez do jogador {jogador}!")
        linha = int(input("Escolha a linha (0,1 ou 2): "))
        coluna = int(input("Escolha a coluna (0,1 ou 2): "))

        if 0<= linha <= 2 and 0<= coluna <=2:
            if posicao_livre(linha, coluna, tabuleiro):
                # Se estiver livre, atualiza o tabuleiro
                tabuleiro[linha][coluna] = f"{jogador}"
                break
            else:
                # Se não estiver livre, avisa o jogador e volta ao início
                print("Posição já ocupada! Tente outra.")
        else:
            print("Posição inválida. Por favor escolha números entre 0 e 2.")

def vencedor(jogador, tabuleiro):
    # Verifica as linhas
    for i in range(3):
        if tabuleiro [i][0] == f"{jogador}" and tabuleiro [i][1] == f"{jogador}" and tabuleiro[i][2] == f"{jogador}":
            return True
    # Verifica as colunas
    for i in range(3):
        if tabuleiro [0][i] == f"{jogador}" and tabuleiro [1][i] == f"{jogador}" and tabuleiro [2][i] == f"{jogador}":
            return True
    # Verifica as diagonais
    if (tabuleiro[0][0] == f"{jogador}" and tabuleiro[1][1] == f"{jogador}" and tabuleiro [2][2] == f"{jogador}") or \
        (tabuleiro[0][2] == f"{jogador}" and tabuleiro[1][1] == f"{jogador}" and tabuleiro[2][0] == f"{jogador}"):
            return True
    return False

# Placar fora do Loop principal
vitoriasX = 0
vitoriasO = 0
empates = 0
total_partidas = 0

# Loop principal (para várias partidas)
while True:
    tabuleiro = [
        ['___', '___', '___'],
        ['___', '___', '___'],
        ['___', '___', '___'],
    ]
    jogador_atual ='_X_'
    jogo_acabou = False

    print ("--- Início do Jogo ---")
    # Loop de uma partida
    for jogada in range(9):
        mostrar_tabuleiro(tabuleiro)
        jogar(jogador_atual, tabuleiro)

        if vencedor(jogador_atual, tabuleiro):
            mostrar_tabuleiro(tabuleiro)
            print(f" --- Fim de Jogo ---")
            print (f"O jogador '{jogador_atual}' venceu!")

            if jogador_atual == '_X_':
                vitoriasX +=1
            else:
                vitoriasO += 1
            jogo_acabou = True
            break

        if jogador_atual == '_X_':
            jogador_atual = '_O_'
        else:
            jogador_atual = '_X_'

    if not jogo_acabou:
        mostrar_tabuleiro(tabuleiro)
        print("--- Fim de Jogo ---")
        print("Deu velha!")
        empates += 1

    # Mostra o placar e pergunta se quer jogar de novo
    print (" --- PLACAR ---")
    print (f"Vitórias de X: {vitoriasX}")
    print (f"Vitórias de O: {vitoriasO}")
    print (f"Empates: {empates}")
    total_partidas += 1

    de_novo = input("Deseja jogar novamente? [s/n] ")
    if de_novo != 's':
        break

print("Obrigado por jogar!")