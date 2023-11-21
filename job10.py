# Initialisation des variables
montant_initial = 10000.0  # Montant initial de l'investissement
taux_rendement_annuel = 5.0  # Taux de rendement annuel en pourcentage

# Affichage du gain annuel initial
gain_annuel = (taux_rendement_annuel / 100) * montant_initial
print("Gain annuel initial :", gain_annuel)

# L'investisseur augmente son capital de 5 000 euros, le taux augmente de 2%
montant_initial += 5000
taux_rendement_annuel += 2

# Calcul du nouveau gain annuel
nouveau_gain_annuel = (taux_rendement_annuel / 100) * montant_initial
print("Nouveau gain annuel après augmentation :", nouveau_gain_annuel)

# L'investisseur retire 10% du montant total, le rendement diminue de 1%
retrait = 0.10 * montant_initial
montant_initial -= retrait
taux_rendement_annuel -= 1

# Calcul du montant final de l'investissement et affichage du nouveau gain
montant_final = montant_initial + nouveau_gain_annuel
print("\nMontant final de l'investissement après retrait :", montant_final)
