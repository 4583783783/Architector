Functiun of PGCD in Python :

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

