# Logical operators
# AND , OR, NOT


#AND
"""a = True
b = True
result = a and b
print(result)"""

""" Anything you put inside here would be seen as a comment """

#OR A must be true and B must be true for result to be true
"""a = True
b = False
result = a or b
print(result)"""


"""#NOT
a = False
result = not(a)
print(result)"""

# All users must be boys
# All users must be 18 and above
"""gender = input("Please enter your gender")
age = int(input("Please enter your age"))

if(gender == "male" and age>=18):
    print("Welcome to our app")
else:
    print("You are not allowed to sign up")"""

"""name = 3.9

print(type(name))"""

#Conditional statement OR iterations
"""if(5<3):
    print("Five is greater than 3")"""

"""
>, <, >=,<=, ==, !=
"""

"""if(5!=4):
    print("This statement is true")
else:
    print("This statement is false")"""

#elif
"""gender = input("Please enter your gender")
if(gender == "male"):
    print("Welcome Mister")
elif (gender == "female"):
    print("Welcome Madam")
elif(gender != "male"):
    print("Strange gender")
elif(gender != "female"):
    print("Strange gender")
else:
    print("Gender unknown")"""

#Loops
#For loop, While loops

"""counter = 0
while counter <10:
    print(counter)
    counter = counter + 1
"""


"""lucky_number = 7
guess = int(input("Please enter your lucky guess"))

while(guess != lucky_number):
    guess = int(input("Please enter your lucky guess"))

print("Hooray! You won $10,000")"""

"""lucky_number = 7
guess = int(input("Please enter your lucky guess"))

while(guess != lucky_number):
    guess = int(input("Please enter your lucky guess"))
    if(guess == lucky_number):
        break

"""

i = 0

while i<6:
    i = i + 1
    if i==3:
        break
    print(i)
