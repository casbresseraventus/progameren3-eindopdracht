
x = input("Wat is het bedrag waar je de btw bij wil berekenen:")

bedrag_excl_btw = float(x)
print( "bedrag (exclusief btw): " + str(bedrag_excl_btw) + "0")

btw = 0.21 * bedrag_excl_btw
btw = (float(btw))
print( "btw (21%): " +  str(btw) + "0")

bedrag_incl_btw = bedrag_excl_btw + btw 
print( "bedrag (inclusief btw): " + str(bedrag_incl_btw) + "0")