import tkinter as tk
from tkinter import ttk
from reistijd_berekenen import ReistijdBerekenaar   # het bestand waar de code is opgeslagen

class reistijd_berekenen(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.reistijd_berekenaar = ReistijdBerekenaar(self)
        self.reistijd_berekenaar.pack(padx=10, pady=10)
        
class omtrek_cirkel(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.reistijd_berekenaar = ReistijdBerekenaar(self)
        self.reistijd_berekenaar.pack(padx=10, pady=10)

class Menu(ttk.Notebook):
    def __init__(self, container):
        super().__init__(container)
        self.main_page = MainPage(self)
        self.add(self.main_page, text='Main Page')

root = tk.Tk()
menu = Menu(root)
menu.pack(expand=True, fill='both')
root.mainloop()