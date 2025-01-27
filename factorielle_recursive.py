# Une variable et sa valeur dans la fonction reste dans la fonction et ne va pas ailleurs sans "return"
#____________________________________________________________

def factorielle(nombre):
    
    if nombre == 1: # condition d'arrêt !!!!
        return 1
    return nombre * factorielle(nombre - 1)
#_____________________________________________________________

# poser la question pour donner un nombre au programme
nombre = int(input("Quel est ton nombre a factoriser ?")) 

# appeller la fonction et la mettre dans v 
v = factorielle(nombre)

# imprimer return
print(v)