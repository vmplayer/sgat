import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("HelpYouOut - Assist. Técnica")
window.geometry("1920x1080")

lbRotulo = tk.Label(
    window,
    text="Nova Ordem de Serviço﹕",
    font=("Arial", 30, "bold"),
    fg="darkblue"
)

img = Image.open("Untitled458_20261126150943.png")
img.thumbnail((600, 240)) 
foto = ImageTk.PhotoImage(img)

label = tk.Label(window, image=foto)
label.pack(pady=5)

lbRotulo.pack(pady=20)

window.mainloop()