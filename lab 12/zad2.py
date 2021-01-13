import math
r = int(input("Podaj promien: "))

def kula(r):
    p = r * 4 * math.pi
    v = 4 / 3 * math.pi * math.pi
    return v and p
print(kula(r))