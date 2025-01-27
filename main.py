import n_premiers as premier
import PGCD as plus_grand_diviseur_commun

nombre_1 = int(input("Quel est ton 1er nombre ?"))
nombre_2 = int(input("Quel est ton 2em nombre ?"))

if premier.nombrePremiers(nombre_1):
    print(nombre_1, " est un nombre premiers")

if premier.nombrePremiers(nombre_2):
    print(nombre_2, " est un nombre premiers")

print(plus_grand_diviseur_commun.pgcd(x=nombre_1, y=nombre_2))
