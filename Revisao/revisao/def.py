def imc(peso, idade, altura):
    imc = peso/(altura*altura)
    return imc

def calculo_imc(peso:float, altura:float)->float:
    return float(peso/(altura*altura))

def calcular_dois_numeros(num1:float, num2:float)->float:
    return float(num1+num2)

def calcular_dois_numeros_try(num1:float, num2:float)->float:
    try:
        return float(num1+num2)
    except:
        return float(1+1)



print(calculo_imc(86.500, 1.78))
imc(90, 32, 1.90)
teste1 = calcular_dois_numeros(10,20)
print(teste1)
teste2 = calcular_dois_numeros_try("A","B")
print(teste2)
#print(notas())

def notas():
    idade = 10
    leo = 20
    felipe = idade + leo / leo
print(notas())#none

def notas1(idade = 0, num2 = 2):
    idade = 10
    leo = 20
    return idade *num2
print(notas1())#none
def notas2():
    idade = 10
    leo = 20
    felipe = idade + leo / leo
    print(felipe)
notas2()#11.0
def notas3():
    idade = 10
    leo = 20
    felipe = idade + leo / leo
    return felipe
print(notas3())#11.0

#daniel = felipe*2
#print(daniel)