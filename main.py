import tkinter as tk

window = tk.Tk()
window.title("HelpYouOut")
window.geometry("1920x1080")

lbRotulo = tk.Label(
    window,
    text="Bem-vindo(a) ao sistema de cadastro.",
    font=("Arial", 30),
    fg="darkblue"
)

lbRotulo.pack(pady=50)

window.mainloop()