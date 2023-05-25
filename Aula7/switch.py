def switch(testador:str, cases:list, returns:list):
    count = 0
    for x in cases:
        if testador == x:
            return returns[count]
        count +=1

# o testador tem que ser o mesmo tipo do caso
test = 10
casos = [1,2,3,4,5,12,14,23,27,10,11,29]
retornos = ['o','ps','sjsj','eu','sdim','nosso','vai','vamo','vem','pois','posso','foram']

d = switch(test, casos, retornos)
print(d)

#--------------------------------------------------------------------