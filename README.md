# Functiun in Python

This is the functiun to PGCD who take 2 numbers and who give the 
most divisor of the 2 numbers

# Fonction en Python

C'est la fonction de PGCD qui prend 2 nombres et qui donne le
plus grand diviseur des 2 nombres

# Función en Python

Esta es la función de PGCD que toma 2 números y da como resultado el
mayor divisor de los 2 números

# Funktion in Python

Dies ist die Funktion für PGCD, die 2 Zahlen nimmt und den 
größten Teiler der 2 Zahlen angibt.


def pgcd(x, y):
    print("calcul pgcd de", x, "et", y, ":")
    result = 0

    for i in range(1, max(x, y)):
        if (x % i == 0) and (y % i == 0):
            result = i
        
    return result

#Exemple
print(pgcd(x=8, y=4))
print(pgcd(x=24, y=8))

