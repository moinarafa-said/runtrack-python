# Définition des variables pour le produit
nom_produit = "tablette"
prix_unitaire = 250.0
quantite_en_stock = 120

# Affichage des informations initiales sur le produit
print("Informations initiales sur le produit :")
print("Nom du produit:", nom_produit)
print("Prix unitaire:", prix_unitaire)
print("Quantité en stock:", quantite_en_stock)

# Ajout de produits en stock
quantite_ajoutee = int(input("Entrez la quantité de produits que vous souhaitez acheter : "))
quantite_en_stock -= quantite_ajoutee

# Mise à jour du prix suite à l'inflation
augmentation_prix = 0.10
prix_unitaire *= (1 + augmentation_prix)

# Affichage des informations après les mises à jour
print("\nInformations après les mises à jour :")
print("Nom du produit:", nom_produit)
print("Nouveau prix unitaire (après inflation de 10%):", prix_unitaire)
print("Nouvelle quantité en stock:", quantite_en_stock)