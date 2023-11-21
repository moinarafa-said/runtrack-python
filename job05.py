# Afficher l'alphabet  à l'envers
for lettre in range(ord('z'), ord('a')-1, -1):
    print(chr(lettre), end=' ')

print()  # Aller à la ligne après l'alphabet en majuscules à l'envers
