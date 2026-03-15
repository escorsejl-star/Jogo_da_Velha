import tkinter as tk
from tkinter import messagebox

# Estado do jogo
jogador_atual = "X"
tabuleiro = [""] * 9

# Verifica vitória
def verificar_vitoria():
    combinacoes = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    
    for a, b, c in combinacoes:
        if tabuleiro[a] == tabuleiro[b] == tabuleiro[c] and tabuleiro[a] != "":
            return tabuleiro[a]
    return None

# Verifica empate
def verificar_empate():
    return "" not in tabuleiro

# Clique do jogador
def clique(pos):
    global jogador_atual
    
    if tabuleiro[pos] == "":
        tabuleiro[pos] = jogador_atual
        botoes[pos]["text"] = jogador_atual
        
        vencedor = verificar_vitoria()
        
        if vencedor:
            messagebox.showinfo("Fim de jogo", f"Jogador {vencedor} venceu!")
            reiniciar()
        elif verificar_empate():
            messagebox.showinfo("Fim de jogo", "Empate!")
            reiniciar()
        else:
            jogador_atual = "O" if jogador_atual == "X" else "X"

# Reinicia o jogo
def reiniciar():
    global tabuleiro, jogador_atual
    tabuleiro = [""] * 9
    jogador_atual = "X"
    for botao in botoes:
        botao["text"] = ""

# Interface gráfica
janela = tk.Tk()
janela.title("Jogo da Velha")

botoes = []

for i in range(9):
    botao = tk.Button(janela, text="", font=("Arial", 20), width=5, height=2,
                      command=lambda i=i: clique(i))
    botao.grid(row=i//3, column=i%3)
    botoes.append(botao)

janela.mainloop()