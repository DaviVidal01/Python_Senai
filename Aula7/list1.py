def lisswitch(testador:list, cases: dict, returns: dict):
    result= []
    for chave in testador:
        if chave : # x = 1 aluno
            count = 0
            for i in cases[chave]: #i = 34 12
                if i == chave:
                    result.append(returns[chave][count])
                count +=1
    return result

test = [1,"DaviVidal01",3,"Github"]
caso = {
    test[0]: [34,12,14,25,37,60,1],
    test[1]: ['fsaf','dgaf','fasf','dfsf','tjt'],
    test[2]: [23,345,34,3],
    test[3]: ['Follow','Star','Repository','Issues']
}
retornos = {
    test[0]: [1,2,3,4,5,6,7],
    test[1]: ['a','b','c','d','f','acertou'],
    test[2]: [12,1,12,'acertou numero'],
    test[3]: [1,2,3,4]
}
a = lisswitch(test,caso,retornos)
print(a)