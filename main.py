import tkinter as tk
from PIL import Image, ImageTk
import customtkinter as ctk

window = tk.Tk()
window.title("HelpYouOut - Assist. Técnica")
window.geometry("1920x1080")

# Quadrado / caixa principal que agrupa tudo
# quadrado = tk.Frame(
#     window,
    
#     bg="#ececec",
#     padx=28,
#     pady=24,
#     highlightthickness=2,
#     highlightbackground="#334155",
#     highlightcolor="#334155",
# )

quadrado = ctk.CTkFrame(
    window,
    fg_color="#ffffff",
    corner_radius=24,      # intensidade do arredondamento
    border_width=2,        # espessura da borda (0 para sem borda)
    border_color="#334155",
    width=480,
    height=340,
)
quadrado.pack(padx=30, pady=30)
quadrado.pack_propagate(False)

    # Centraliza a caixa na janela com um padding (espaçamento) em volta :)

img = Image.open("Untitled458_20261126150943.png")
img.thumbnail((600, 240)) 
foto = ImageTk.PhotoImage(img)

label = tk.Label(window, image=foto)
label.pack(pady=5)

tk.Label(
    quadrado,
    text="Nova Ordem de Serviço﹕",
    font=("Arial", 30, "bold"),
    fg="darkblue",
)

tk.Label.pack(pady=0)

# Contêiner para organizar o formulário em linhas e colunas e manter mais organizadinho (um container?!?)
frForm = tk.Frame(quadrado)
frForm.pack(pady=10)

lbCliente = tk.Label(frForm, text="Cliente:", font=("Arial", 12, "bold"))
lbCliente.grid(row=0, column=0, padx=(0, 8), pady=5, sticky="e")

enCliente = tk.Entry(frForm, width=30, font=("Arial", 11))
enCliente.grid(row=0, column=1, pady=5)

lbTelefone = tk.Label(frForm, text="Telefone:", font=("Arial", 12, "bold"))
lbTelefone.grid(row=1, column=0, padx=(0, 8), pady=5, sticky="w")

enTelefone = tk.Entry(frForm, width=30, font=("Arial", 11))
enTelefone.grid(row=1, column=1, pady=5)

lbEquip = tk.Label(frForm, text="Equipamento:", font=("Arial", 12, "bold"))
lbEquip.grid(row=2, column=0, padx=(0, 8), pady=5, sticky="e")

enEquip = tk.Entry(frForm, width=30, font=("Arial", 11))
enEquip.grid(row=2, column=1, pady=5)

lbMarca = tk.Label(frForm, text="Marca/Modelo:", font=("Arial", 12, "bold"))
lbMarca.grid(row=3, column=0, padx=(0, 8), pady=5, sticky="e")

enMarca = tk.Entry(frForm, width=30, font=("Arial", 11))
enMarca.grid(row=3, column=1, pady=5)

lbValor = tk.Label(frForm, text="Valor:", font=("Arial", 12, "bold"))
lbValor.grid(row=4, column=0, padx=(0, 8), pady=5, sticky="w")

enValor = tk.Entry(frForm, width=30, font=("Arial", 11))
enValor.grid(row=4, column=1, pady=5)

window.mainloop()

