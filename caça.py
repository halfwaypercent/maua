import random
import time
import os
import sys
from dataclasses import dataclass
from typing import List, Tuple, Dict

# ========= Configurações do Jogo =========
SPIN_CUSTO = 1           # Custo por giro em PONTOS (não é dinheiro!)
ANIM_FRAMES = 8          # Quantidade de quadros da animação de giro
ANIM_DELAY = 0.08        # Atraso entre quadros (segundos)
INICIO_PONTOS = 5       # Pontos iniciais

# Símbolos do caça-níquel e seus pesos (probabilidade relativa)
SIMBOLOS = ["🍒", "🍋", "🍉", "🔔", "⭐", "7️⃣"]
PESOS =    [  30 ,   25 ,   20 ,   12 ,   8 ,   5 ]  # total = 100

# Pagamentos por trinca (3 símbolos iguais) encontrados em uma linha válida
# Esses valores são em PONTOS (sem valor real).
PAGAMENTOS = {
    "🍒": 1,
    "🍋": 2,
    "🍉": 3,
    "🔔": 5,
    "⭐": 7,
    "7️⃣": 25,
}

# Linhas válidas (paylines): 3 linhas, 3 colunas e 2 diagonais
PAYLINES = [
    # Linhas (row, col)
    [(0,0), (0,1), (0,2)],
    [(1,0), (1,1), (1,2)],
    [(2,0), (2,1), (2,2)],
    # Colunas
    [(0,0), (1,0), (2,0)],
    [(0,1), (1,1), (2,1)],
    [(0,2), (1,2), (2,2)],
    # Diagonais
    [(0,0), (1,1), (2,2)],
    [(0,2), (1,1), (2,0)],
]

# ========= Utilidades de Terminal =========
def limpar_terminal():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception:
        pass

def pause(seg=0.4):
    try:
        time.sleep(seg)
    except KeyboardInterrupt:
        pass

def color(txt, c):
    # Cores simples ANSI (se não suportar, retorna texto cru)
    if sys.stdout.isatty():
        cores = {
            "verde": "\033[92m",
            "amarelo": "\033[93m",
            "azul": "\033[94m",
            "magenta": "\033[95m",
            "ciano": "\033[96m",
            "vermelho": "\033[91m",
            "reset": "\033[0m",
            "negrito": "\033[1m",
        }
        return f"{cores.get(c,'')}{txt}{cores['reset']}"
    return txt

# ========= Núcleo do jogo =========
@dataclass
class ResultadoLinha:
    linha: List[Tuple[int,int]]
    simbolo: str
    ganho: int

def sorteia_simbolo() -> str:
    return random.choices(SIMBOLOS, weights=PESOS, k=1)[0]

def gira_tabuleiro() -> List[List[str]]:
    return [[sorteia_simbolo() for _ in range(3)] for _ in range(3)]

def verifica_trincas(grid: List[List[str]]) -> List[ResultadoLinha]:
    resultados = []
    for linha in PAYLINES:
        s1 = grid[linha[0][0]][linha[0][1]]
        s2 = grid[linha[1][0]][linha[1][1]]
        s3 = grid[linha[2][0]][linha[2][1]]
        if s1 == s2 == s3:
            ganho = PAGAMENTOS.get(s1, 0)
            resultados.append(ResultadoLinha(linha=linha, simbolo=s1, ganho=ganho))
    return resultados

def desenha_grid(grid: List[List[str]], highlight: List[Tuple[int,int]] = None):
    highlight = set(highlight or [])
    linhas = []
    for r in range(3):
        row_syms = []
        for c in range(3):
            sy = grid[r][c]
            if (r, c) in highlight:
                row_syms.append(color(f"[{sy}]", "amarelo"))
            else:
                row_syms.append(f" {sy} ")
        linhas.append(" │ ".join(row_syms))
    print("┌───┬──┬──────┬───┬──┐")
    print("│ " + linhas[0] + " │")
    print("├───┼──┼──────┼───┼──┤")
    print("│ " + linhas[1] + " │")
    print("├───┼──┼──────┼───┼──┤")
    print("│ " + linhas[2] + " │")
    print("└───┴──┴──────────┴──┘")

def anima_giro():
    for i in range(ANIM_FRAMES):
        fake = [[random.choice(SIMBOLOS) for _ in range(3)] for _ in range(3)]
        limpar_terminal()
        print(color("Girando...", "azul"))
        desenha_grid(fake)
        pause(ANIM_DELAY)

def mostrar_tabela():
    print(color("\nTabela de Pagamentos (trincas 3 em linha):", "negrito"))
    for s in SIMBOLOS:
        print(f"  {s}  -> {PAGAMENTOS[s]} pontos")
    print(color("\nLembrete: isto é apenas um jogo de DIVERSÃO por pontos (sem dinheiro real).", "ciano"))

def instrucoes():
    print(color("Caça-Níquel de Diversão 🎰", "negrito"))
    print("Sem apostas reais. Você joga por PONTOS.")
    print(f"Pontos iniciais: {INICIO_PONTOS} | Custo por giro: {SPIN_CUSTO} ponto")
    print("Comandos: [S]pin  [T]abela  [R]einiciar  [Q]uitar")

def main():
    pontos = INICIO_PONTOS
    random.seed()
    limpar_terminal()
    instrucoes()
    mostrar_tabela()

    while True:
        print(color(f"\nSeus pontos: {pontos}", "verde"))
        cmd = input(color("Digite (S/T/R/Q): ", "magenta")).strip().lower()

        if cmd == "q":
            print(color("Valeu por jogar! Até a próxima. ✨", "ciano"))
            break
        elif cmd == "t":
            mostrar_tabela()
            continue
        elif cmd == "r":
            pontos = INICIO_PONTOS
            limpar_terminal()
            instrucoes()
            continue
        elif cmd != "s":
            print("Comando inválido.")
            continue

        if pontos < SPIN_CUSTO:
            print(color("Sem pontos suficientes. Reinicie (R) para ganhar pontos novamente.", "vermelho"))
            continue

        # Cobra o custo do giro
        pontos -= SPIN_CUSTO

        # Anima e gira
        anima_giro()
        grid = gira_tabuleiro()

        limpar_terminal()
        instrucoes()
        print(color("\nResultado do giro:", "negrito"))
        desenha_grid(grid)

        # Verifica ganhos
        resultados = verifica_trincas(grid)
        if not resultados:
            print(color("Nenhuma trinca desta vez. Boa sorte no próximo giro!", "vermelho"))
        else:
            total = sum(r.ganho for r in resultados)
            print(color("\nVocê conseguiu trinca(s)!", "verde"))
            for r in resultados:
                print(f"  Linha {[(rr,cc) for rr,cc in r.linha]}  {r.simbolo}  +{r.ganho} pontos")
            print(color(f"Total ganho: +{total} pontos", "verde"))
            pontos += total

        # Dica extra quando pontos acabam
        if pontos <= 0:
            print(color("\nVocê ficou sem pontos. Use (R) para reiniciar e continuar se divertindo!", "amarelo"))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSaindo... Até a próxima!")