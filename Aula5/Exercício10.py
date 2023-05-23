n = int(input("Fatorial de: "))
r = 1
for ix in range(1,n+1,1):
    r *= ix
print("O FATORIAL DE {} É {}".format(n,r))