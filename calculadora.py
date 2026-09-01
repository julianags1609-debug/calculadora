import tkinter as tk

# =========================
# JANELA
# =========================

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("370x550")
janela.resizable(False, False)

# Cores
AZUL = "#000237"
LARANJA = "#010100"
BRANCO = "#A19D9D"
PRETO = "#000000"

janela.configure(bg=AZUL)

# VISOR

visor = tk.Entry(
    janela,
    font=("Arial", 28),
    bg=AZUL,
    fg="white",
    bd=0,
    relief="flat",
    justify="right"
)

visor.grid(
    row=0,
    column=0,
    columnspan=4,
    sticky="nsew"
)


# =========================
# FUNÇÕES
# =========================

def clicar(valor):
    atual = visor.get()

    # Se estiver aparecendo Erro, começa novamente
    if atual == "Erro":
        atual = ""

    visor.delete(0, tk.END)
    visor.insert(0, atual + str(valor))


def limpar():
    visor.delete(0, tk.END)


def excluir():
    atual = visor.get()

    visor.delete(0, tk.END)
    visor.insert(0, atual[:-1])


def calcular():
    try:
        expressao = visor.get()

        resultado = eval(expressao)

        visor.delete(0, tk.END)
        visor.insert(0, resultado)

    except:
        visor.delete(0, tk.END)
        visor.insert(0, "Erro")


def porcentagem():
    try:
        valor = float(visor.get()) / 100

        visor.delete(0, tk.END)
        visor.insert(0, valor)

    except:
        visor.delete(0, tk.END)
        visor.insert(0, "Erro")


# =========================
# CONFIGURAÇÃO DA GRADE
# =========================

for coluna in range(4):
    janela.grid_columnconfigure(coluna, weight=1)

janela.grid_rowconfigure(0, weight=2)

for linha in range(1, 6):
    janela.grid_rowconfigure(linha, weight=1)


# CRIAR BOTÕES

def criar_botao(texto, linha, coluna, comando,
                cor=BRANCO, texto_cor=PRETO,
                coluna_span=1):

    botao = tk.Button(
        janela,
        text=texto,
        font=("Arial", 18),
        bg=cor,
        fg=texto_cor,
        bd=1,
        relief="solid",
        command=comando
    )

    botao.grid(
        row=linha,
        column=coluna,
        columnspan=coluna_span,
        sticky="nsew",
        padx=1,
        pady=1
    )

# PRIMEIRA LINHA
# C | ⌫ | % | /

criar_botao(
    "C",
    1,
    0,
    limpar
)

criar_botao(
    "⌫",
    1,
    1,
    excluir
)

criar_botao(
    "%",
    1,
    2,
    porcentagem
)

criar_botao(
    "/",
    1,
    3,
    lambda: clicar("/"),
    LARANJA,
    "white"
)


# =========================
# 7 | 8 | 9 | *
# =========================

criar_botao("7", 2, 0, lambda: clicar("7"))
criar_botao("8", 2, 1, lambda: clicar("8"))
criar_botao("9", 2, 2, lambda: clicar("9"))

criar_botao(
    "*",
    2,
    3,
    lambda: clicar("*"),
    LARANJA,
    "white"
)


# =========================
# 4 | 5 | 6 | -
# =========================

criar_botao("4", 3, 0, lambda: clicar("4"))
criar_botao("5", 3, 1, lambda: clicar("5"))
criar_botao("6", 3, 2, lambda: clicar("6"))

criar_botao(
    "-",
    3,
    3,
    lambda: clicar("-"),
    LARANJA,
    "white"
)


# =========================
# 1 | 2 | 3 | +
# =========================

criar_botao("1", 4, 0, lambda: clicar("1"))
criar_botao("2", 4, 1, lambda: clicar("2"))
criar_botao("3", 4, 2, lambda: clicar("3"))

criar_botao(
    "+",
    4,
    3,
    lambda: clicar("+"),
    LARANJA,
    "white"
)


# =========================
# 0 | . | =
# =========================

criar_botao(
    "0",
    5,
    0,
    lambda: clicar("0"),
    coluna_span=2
)

criar_botao(
    ".",
    5,
    2,
    lambda: clicar(".")
)

criar_botao(
    "=",
    5,
    3,
    calcular,
    LARANJA,
    "white"
)

# INICIAR

janela.mainloop()