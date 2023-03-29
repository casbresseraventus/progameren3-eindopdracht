import math
import tkinter as tk

# Functie om de berekeningen uit te voeren
def berekenen():
    x = int(diameter_entry.get())
    omtrek = math.pi * x
    straal = x / 2
    oppervlakte = straal * 2 * math.pi
    omtrek_label.config(text=f"De omtrek van uw cirkel is: {omtrek}")
    oppervlakte_label.config(text=f"De oppervlakte van uw cirkel is: {oppervlakte}")

# Maak het basisvenster
root = tk.Tk()
root.title("Cirkelberekeningen")

# Maak het invoerveld voor de diameter
diameter_label = tk.Label(root, text="Wat is de diameter?")
diameter_label.pack()
diameter_entry = tk.Entry(root)
diameter_entry.pack()

# Maak de knop om de berekeningen uit te voeren
bereken_button = tk.Button(root, text="Bereken", command=berekenen)
bereken_button.pack()

# Maak de labels voor de uitvoer
omtrek_label = tk.Label(root, text="")
omtrek_label.pack()
oppervlakte_label = tk.Label(root, text="")
oppervlakte_label.pack()

# Start de GUI
root.mainloop()
