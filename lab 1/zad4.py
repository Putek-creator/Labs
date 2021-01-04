godz = 60 * 60 # godzina
doba = godz * 24 #doba
rok1 = 365 * doba #nieprzystepny
rok2 = 366 * doba #przystepny
a = float(input("Ile masz lat:"))
print("Tyle sekund ma Twoje życie:",rok1 * a )