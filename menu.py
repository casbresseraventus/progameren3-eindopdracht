import tkinter as tk
from tkinter import messagebox
from reistijd_berekenen import ReistijdBerekenaar
from omtrek_cirkel import berekenen

# functies voor de programma's
def program1():
    messagebox.showinfo("Programma 1", "Dit is programma 1.")

def program2():
    messagebox.showinfo("Programma 2", "Dit is programma 2.")

# GUI initialisatie
root = tk.Tk()
root.geometry("500x500")
# menu maken
menu_bar = tk.Menu(root)

# submenu's maken
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Programma 1", command=ReistijdBerekenaar)
file_menu.add_command(label="Programma 2", command=berekenen)

# submenu's aan menubalk toevoegen
menu_bar.add_cascade(label="Programma's", menu=file_menu)

# menubalk aan root window toevoegen
root.config(menu=menu_bar)

# GUI starten
root.mainloop()
