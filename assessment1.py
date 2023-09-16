"""
GRADE CALCULATOR
1. Collect the score of a student
2. is going assign a grade based on the score of the student
GRADE TABLE
A : 90 and above
B : 80 to 89
C : 70 to 79
D : 60 to 69
E : 50 to 59
F : 0 to 49

"""
"""ahead = True

while ahead:

    score = int(input("Please enter your score"))


    if score >= 70 and score <= 100:
        print("GRADE = A")

    elif score >= 60 and score <= 69:
        print("GRADE = B")
    elif score >= 55 and score <= 59:
        print("GRADE = C")
    elif score >= 46 and score <= 54:
        print("GRADE = D")
    elif score >= 40 and score <= 45:
        print("GRADE = E")
    elif score >= 0 and score <= 39:
        print("GRADE = F")
    else:
        print("You entered the wrong score")

    feedback = input("Do you want to proceed? y / n")
    if (feedback == 'y'):
        ahead = True
    else:
        ahead = False"""


"""user_input = input("Is it raining? y/n")

if user_input == "y":
    print("Please carry an umbrella")

elif user_input == "n":
    print("Please take your sun shades")
else:
    print("You entered a wrong character")"""

#Nest if else statement
"""raining = False
wind = False
if raining == True:
    if wind == True:
        print("It is rainy and windy")
    else:
        print("It is rainy but not windy")
elif wind == True:
    print("It is not raining but windy")
else:
    print("it is not rainy and not windy")"""


"""shopping = ["apple", "orange", "milk", "milo", "bread"]
#print(shopping[2] + " & " + shopping[3])

for i in shopping:
    print(i)"""
"""
for i in "Samuel":
    print(i)"""

"""name = "Samuel"

for i in name:
    print(i)
"""
#list
"""shopping = ["apple", "orange", "milk", "milo", "bread"]
numbers = [ 33,65,13,7,90,67,37]"""

#dictionary - these are key value pairs
"""grades = {"A": 70, "B": 60, "C": 50, "D":40, "E": 30, "F": 20}

print(grades["C"])
grades.pop("F")
print(grades)
print(grades.keys())

for i in grades.keys():
    print(i)
"""
"""
print(numbers)
print( len(numbers)  )
print(min(numbers))
print(max(numbers))
shopping.append("ice cream")
print(shopping)

numbers.append(132)
print(numbers)
print(max(numbers))"""

#Task to be submitted on tuesday
#Creat a todo list for your day and save it in a list.
#Then at the end of your program, display all the values of your todo list.
"""status = True
todo_list = []
while status:
    check = input("Do you have an additional item to add to your todo? y/n")
    if check == "y":
        item = input("Please enter a todo item")
        todo_list.append(item)
    elif check == "n":
        print("These are your todo items for today")
        for i in todo_list:
            print(i)
        break


"""

