v = ", "
par = ""
for ix in range(100,401,1):
    if ix % 2 == 0:
        par = par + str(ix)
        if ix != 400:
           par = par + v
print(f"{par}")