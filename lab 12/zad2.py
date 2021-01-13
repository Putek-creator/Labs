import math
r = int(input("Podaj promien: "))
def kula(r):
    p = math.pow(r,2) * 4 * math.pi
    v = 4/3 * math.pi * math.pow(r,3)
    print("Pole to ",p,", objętośc to", v)
print(kula(r))