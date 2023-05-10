tuplas = ()
tuplad = (1,2,"oi","teste",[1.3,5,"titototot", 'tltmsdkds'])
print(type(tuplas))
print(tuplad)

#Forma de burlar o sistema de Tuplas
lista = [1,2,3,4,5]
tup = (lista)
print(tup)
lista.append(6)
print(tup)