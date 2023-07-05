#estrutura ranger range(cond1, cond2, cond3)
#pirmeira cond é o inicializador se você não passar ele automaticamente começa em 0
# o segundo é o finalizador até aonde você quer que ele vá
# O terceiro é o pulo de quanto em quanto se você não passar nada ele automaticamente fica de 1 em 1
range(1,10,1)
print(range(1,10,1))#lembresse ele so exibe com lista
print(list(range(1,10,1)))

#laço for
# logo após escreva uma variavel e depois o in e até o finalizador
for i in range(1, 10):
    print(i)
#com estrutura de dados
l = ['Igor','teste','oi']
for i in l:
    print(i)
#com string
o = "igor"
for i in o:
    print(i)
#com condição usando modulo
for i in range(100):
    if i % 2 == 0:
        print("{} é par".format(i))


# estrutura de laço while
#na estrutura de while ele testa se o codigo é verdadeira ele realiza algo
x = 0
while x < 10:
    print("O valor de x é : {}".format(x))
    x +=1 # x=x+1


# com o else 
while x < 10:
    print("O valor de z é : {}".format(x))
    print("X ainda é menor que 10. Incrementado...")
    x +=1 
else:
    print("Concluido primeiro while")


#utilizando o continue
while x < 10:
    print("O valor de u é : {}".format(x))
    continue
    print("X ainda é menor que 10. Incrementado...")
    x +=1 
else:
    print("Concluido segundo while")

#utilizando o break
while x < 10:
    print("O valor de x é : {}".format(x))
    x +=1 
    break
    print("X ainda é menor que 10. Incrementado...")
    
