print("Números Divisíveis por 7 do 5 a 100:")
sete = 7
for ix in range(5,101,1):
    if ix % 7 == 0 and ix % 5 != 0:
      print("{} é Divisível por 7".format(ix))
