import math
import tkinter as tk

class CircleCalculator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Maak het invoerveld voor de diameter
        self.diameter_label = tk.Label(self, text="Wat is de diameter?")
        self.diameter_label.pack()
        self.diameter_entry = tk.Entry(self)
        self.diameter_entry.pack()

        # Maak de knop om de berekeningen uit te voeren
        self.bereken_button = tk.Button(self, text="Bereken", command=self.berekenen)
        self.bereken_button.pack()

        # Maak de labels voor de uitvoer
        self.omtrek_label = tk.Label(self, text="")
        self.omtrek_label.pack()
        self.oppervlakte_label = tk.Label(self, text="")
        self.oppervlakte_label.pack()

    # Functie om de berekeningen uit te voeren
    def berekenen(self):
        x = int(self.diameter_entry.get())
        omtrek = math.pi * x
        straal = x / 2
        oppervlakte = straal * straal * math.pi

        # update the labels with the calculated values
        self.omtrek_label.config(text="De omtrek is {:.2f}".format(omtrek))
        self.oppervlakte_label.config(text="De oppervlakte is {:.2f}".format(oppervlakte))

# Create the root window and start the mainloop
#root = tk.Tk()
#app = CircleCalculator(master=root)
#app.mainloop()
