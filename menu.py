import tkinter as tk
from tkinter import messagebox

from reistijd_berekenen import ReistijdBerekenaar
from omtrek_cirkel import CircleCalculator
from vierkant import VierkantBerekenaar

# GUI initialisatie

root = tk.Tk()
# menu maken
menu_bar = tk.Menu(root)

# submenu's maken
file_menu = tk.Menu(menu_bar)

file_menu.add_command(label="reistijd berekenaar", command= ReistijdBerekenaar)
file_menu.add_command(label="cirkel berekenaar", command= CircleCalculator)
file_menu.add_command(label="vierkant berekenaar", command= VierkantBerekenaar)

# submenu's aan menubalk toevoegen
menu_bar.add_cascade(label="Programma's", menu=file_menu)
 
# menubalk aan root window toevoegen
root.config(menu=menu_bar)
 
# GUI starten
root.mainloop()
 