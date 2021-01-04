foot = 30.48
a = int(input("Podaj ilosc stop: "))
print(f"Wysokość w cm", foot * a)
print(f"Wysokość w m ", foot / 100 * a)
print(f"Wysokość w mm {foot*10*a}")
print(f"Wysokość w km {foot/1000*a}")