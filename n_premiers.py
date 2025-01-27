
#__________________________
def nombrePremiers(x):
    result = True
    for z in range(2, int(x / 2)):
        if (x % z == 0):
            return False
    return result
#__________________________

# Main program

