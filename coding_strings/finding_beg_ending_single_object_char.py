data = "aabbcddeefghikk"

y = ""
z = ""
for x in data:
    if y == "":
        y = x
    elif y == x:
        y = ""
for x in data[::-1]:
    if z == "":
        z = x
    elif z== x:
        z = ""
print(y+z)
