from pytemp import pytemp
temp = int(input(("Podaj temperaturę w C: ")))
f  = pytemp(temp,'c','f')
print("Temp w F =", f)
if f >= 212:
    print("woda wrze")
elif f <= 32:
    print("woda zamarza")
#Kelvin -> Fahrenheit
f = pytemp(40,'k', 'f')
#Fahrenheit -> Kelvin
k = pytemp(f,'f','k')
#Celcius -> Kelvin
c = pytemp(40,'k', 'c')
#Kelvin -> Celcius
k1 = pytemp(c,'c','k')