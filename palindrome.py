
#____1________________________________________________________________
def greeting(prenom):
    print("Bonjour", prenom, "j'espère que tu vas bien !")
#______________________________________________________________________

#_____2_________________________________________________________________
def isPalindrome(mot):
    if mot == mot[::-1]:
        print("Le mot", mot, "est un palindrome !")
    else:
        print("Le mot", mot, "est un anacyclique !")
#______________________________________________________________________


# # poser la question pour obtenir un nom
# prenom = str(input("Quel est ton nom ?"))

# #appeler la procedure 1
# greeting(prenom)

# poser la question pour obtenir un mot
mot = str(input("Quel est ton mot ?"))

#appeler la procedure 2
isPalindrome(mot)