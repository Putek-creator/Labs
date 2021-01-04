contacts = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'k': 9,
    'i': 10,
}
x = len(contacts)
print(contacts)
contacts['a'] = 2
print(contacts)
if x % 2 != 0:
    del contacts[x/2]
print(contacts)