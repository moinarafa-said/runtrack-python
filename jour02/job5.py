# parcourir les nbre de 1 à 100 
for nbr in range(1, 101):
    if nbr % 3 == 0 and nbr % 5 == 0: #si le nbr est multiple de 3 et 5
        print("FizzBuzz")
    elif nbr % 3 == 0: # si le nbr est multiple de 3
        print("Fizz")
    elif nbr % 5 == 0: #si le nbr est multiple de 5
        print("Buzz")
    else:
        print(nbr)

