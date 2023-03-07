#Python funcion to find the Max of three nr
def max_of_two(x, y):
    if x > y:
        return x
    return y
def max_of_three(x, y, z):
    return max_of_two(x, max_of_two(y, z))
print(max_of_three(8, 65, 987))

#Python program to reverse a string
txt = "This is homework" [: : -1]
print(txt)

#If variables are equal, print message, otherwise, different message.
x = 78
y = 90
if x == y :
    print("Variables are the same")
else:
    print("Variables are not the same")

#Program to ask for name and age for nightclub
print("Your name please")
name = input()
age = int(input("Your age please"))
timeleft = 18 - age
if age < 18 :
    print("You cannot enter the club, please go home")
else:
    print("Welcome to the party!")