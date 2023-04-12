import tkinter as tk

from tkinter import *

root = Tk()
menubar = Menu(root)

root.geometry("500x500")
root.title("BTW")

label = tk.Label(root, text="BTW Berekenen", font=('Arial', 18))
label.pack(padx=15, pady=15) 

myentry = tk.Entry(root)
myentry.pack()
Button = tk.Button(root, text="Bereken", font=('Arial', 18))
Button.pack()

x = input("Wat is het bedrag waar je de btw bij wil berekenen:")

bedrag_excl_btw = float(x)
print( "bedrag (exclusief btw): " + str(bedrag_excl_btw) + "0")

btw = 0.21 * bedrag_excl_btw
btw = (float(btw))
print( "btw (21%): " +  str(btw) + "0")

bedrag_incl_btw = bedrag_excl_btw + btw 
print( "bedrag (inclusief btw): " + str(bedrag_incl_btw) + "0")

root = Tk()
menubar = Menu(root)