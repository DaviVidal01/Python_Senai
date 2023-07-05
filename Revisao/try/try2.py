a = 100
b = 0

try:
    print(a/b)
except ZeroDivisionError as error:
    print(error)
finally:
    print("Essa parte sempre será executada.")