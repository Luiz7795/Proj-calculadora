import tkinter as tk
from tkinter import messagebox

# mensagens de erro:

def bin_to_dec():
    bin_value = entry.get()
    try:
        decimal = int(bin_value, 2)
        result_label.config(text=f"Decimal: {decimal}")
    except ValueError:
        messagebox.showerror("Erro", "Digite um número binário válido (apenas 0 e 1)")

def dec_to_bin():
    dec_value = entry.get()
    try:
        decimal = int(dec_value)
        binary = bin(decimal)[2:]
        result_label.config(text=f"Binário: {binary}")
    except ValueError:
        messagebox.showerror("Erro", "Digite um número decimal válido (apenas dígitos 0-9)")


root = tk.Tk() # abre a janela da calculadora
root.title("Conversor Binário <-> Decimal")
root.geometry("300x200")


tk.Label(root, text="Digite o número:", font=("Arial", 12)).pack(pady=10) # título
 

entry = tk.Entry(root, font=("Arial", 12)) # campo de entrada dos dígitos
entry.pack()


tk.Button(root, text="Binário → Decimal", command=bin_to_dec).pack(pady=5) # botões de conversão (decimal,binário)
tk.Button(root, text="Decimal → Binário", command=dec_to_bin).pack(pady=5)


result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue") # resultado
result_label.pack(pady=10)


root.mainloop() # iniciar
