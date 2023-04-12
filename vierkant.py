import tkinter as tk

class VierkantBerekenaar(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.info_label = tk.Label(self, text="Geef de lengte:")
        self.info_label.grid(row=0, column=0, padx=5, pady=5)
        self.info_entry = tk.Entry(self)
        self.info_entry.grid(row=0, column=1, padx=5, pady=5)

        self.info2_label = tk.Label(self, text="Geef de breedte:")
        self.info2_label.grid(row=1, column=0, padx=5, pady=5)
        self.info2_entry = tk.Entry(self)
        self.info2_entry.grid(row=1, column=1, padx=5, pady=5)

        self.bereken_button = tk.Button(self, text="Bereken", command=self.bereken_vierkant)
        self.bereken_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.resultaat_label = tk.Label(self, text="")
        self.resultaat_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def bereken_vierkant(self):
        info = int(self.info_entry.get())
        info2 = int(self.info2_entry.get())

        omtrek = info + info2
        opervlakte = info * info2

        result_text = f"Omtrek is {omtrek}\nOpervlakte is {opervlakte}"
        self.resultaat_label.config(text=result_text)

#root = tk.Tk()
#app = VierkantBerekenaar(master=root)
#app.mainloop()
