# A variable and its value in the function stays in the function and does not go elsewhere without "return"
#____________________________________________________________

def factorial(number):
result = 1
for i in range(1, number + 1): # as the range will stop at 4 we put +1 to go up to 5 and conclude the factorial
result = i * result

return result
#_____________________________________________________________

# ask the question to give a number to the program
number = int(input("What is your number to factorize?"))

# call the function and put it in v
v = factorial(number)

# print return
print(v)
