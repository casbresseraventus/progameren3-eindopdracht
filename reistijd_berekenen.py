import tkinter as tk

class ReistijdBerekenaar(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.afstand_label = tk.Label(self, text="Afstand (km):")
        self.afstand_label.grid(row=0, column=0)
        self.afstand_entry = tk.Entry(self)
        self.afstand_entry.grid(row=0, column=1)

        self.snelheid_label = tk.Label(self, text="Snelheid (km/u):")
        self.snelheid_label.grid(row=1, column=0)
        self.snelheid_entry = tk.Entry(self)
        self.snelheid_entry.grid(row=1, column=1)

        self.bereken_button = tk.Button(self, text="Bereken", command=self.bereken_tijd)
        self.bereken_button.grid(row=2, column=0, columnspan=2)

        self.resultaat_label = tk.Label(self, text="")
        self.resultaat_label.grid(row=3, column=0, columnspan=2)

    def bereken_tijd(self):
        afstand = float(self.afstand_entry.get())
        snelheid = float(self.snelheid_entry.get())
        tijd = afstand / snelheid
        self.resultaat_label.config(text="Je bent {} uur onderweg.".format(round(tijd, 2)))

root = tk.Tk()
app = ReistijdBerekenaar(master=root)
app.mainloop()
