grid = [
    [0,1,2], [3,4,5], [6,7,8],  # linhas
    [0,3,6], [1,4,7], [2,5,8],  # colunas
    [0,4,8], [2,4,6] # diagonais
    ]            
estado = [None] * 9
jogador_atual = "X"

def fazer_jogada(index):
    global jogador_atual
    if estado[index] is None:
        if jogador_atual == "X":
            simbolo = "X"
            estado[index] = jogador_atual
            jogador_atual = "O"
        else:
            simbolo = "O"
            estado[index] =  jogador_atual
            jogador_atual = "X"
        return {
            "valida": True,
            "simbolo" :  simbolo
        }
    else:
        return {
            "valida": False,
            "simbolo" :  None
        }

def verificar_vitoria():
    for comb in grid:
        a = comb[0]
        b = comb[1]
        c = comb[2]
        if estado[a] is not None and estado[a] == estado[b] == estado[c]:
            return f"{estado[a]} venceu!"
    if None in estado:
        return None
    else:
        return "Empate!"

def resetar():
    global estado
    global jogador_atual
    
    estado = [None] * 9
    jogador_atual = "X"