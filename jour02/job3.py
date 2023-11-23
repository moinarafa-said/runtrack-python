# Parcourir les nombres de 0 à 100
for nombre in range(101):
    # Exclure les nombres spécifiques 26, 37, 88
    if nombre not in [26, 37, 88]:
        print(nombre)
