def lisswitch(testador:list,cases:dict, returns:dict):
    result = []
    for chave in testador:
        if chave: # x = 1 aluno
            count = 0
            for i in cases[chave]: # i = 34 12
                result.append(returns[chave][count])
            count +=1
    return result

# indice 0, 1
test = ['DaviVidal01', 'Github1']
caso = {
    test[0]: ['DaviVidal01', 'Davi','Vidal'],
    test[1]: ['Star','Repository','Git'],
}
retornos = {
    test[0]: [18,13,12],
    test[1]: [20,30,7],
}

a = lisswitch(test, caso, retornos)
print(a)