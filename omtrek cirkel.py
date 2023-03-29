import math

x = input("wat is de diameter?\n")
x = int(x)

omtrek = math.pi * x
omtrek = str(omtrek)

straal = x / 2

oppervlakte = straal * 2 * math.pi
oppervlakte = str(oppervlakte)

print ("de omtrek van uw cirkel is: " + omtrek + "\n" "en de oppervlakte: " + oppervlakte)