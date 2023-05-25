a = 10
match a:
    case 1:
        print(1)
    case 2:
        print(2)
    case 10:
        print("Você acertou!")
    case _:
        print("Somenthing's wrong with the internet")

def teste(x):
    match x:
        case 20:
            return 2
        case 40:
            return 5
        case 10:
            return "função executada."


def mat(x,c,v,ix,q):
    for ix in range(ix,q):
        if c == "==":
            if x == 1:
                return "X == 1"
        if c == ">=":
            if x >= 1:
                return "X >= 1"
        if c == "<=":
            if x <= 1:
                return "X <= 1"
    

h = teste(a)
print(h)