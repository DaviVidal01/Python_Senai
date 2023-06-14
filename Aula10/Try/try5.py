a = int(input())
b = int(input())

try:
    print(a/b)
except (TypeError,ZeroDivisionError) as error:
    pass
