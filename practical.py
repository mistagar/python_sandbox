'''
- variables
- numbers
- casting
- strings
- operators
- list
- tuples
- dictionaries
- conditionals (if-else, while)
- functions
- classes and objects
- Python Dates
- Python Math functions

- Python Try Except
'''





'''
fruits = ["orange", "apple", "bannana","carrot"]
fruits.append("mango")
fruits.insert(1,"avocado")
fruits.remove("bannana")
fruits.pop()
del fruits[0]
fruits.clear()

print(fruits)
'''


'''vegetable = ("spinach", "carrot", "cabbage", "cuccumber")
for i in vegetable:
    print(i)

if "carrot" in vegetable:
    print("it exists")

print(len(vegetable))

del vegetable

print(vegetable)'''


'''student = {
    "firstname":"Samuel",
    "lastname":"Ejeke",
    "Weight":"66kg",
    "Religion":"Christian"
}
'''
'''student["color"] = "Black"
student.pop("Religion")

#student.clear()
student["Weight"] = "70kg"

for i in student:
    print(student[i])
'''

'''fruits = ["apple", "mango", "orange", ]
veggies = ["cabbage", "cuccumber", "carrot"]

for i in fruits:
    for j in veggies:
        print(i,j)'''

'''def my_function(our_name="Gar"):
    return("Hello " + our_name)

a = my_function("Shalom")
b = my_function("Chidima")
c = my_function("Endurance")
d = my_function("Samuel")

print(a,b,c,d)'''

'''class fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def myfunction(self):
        print("The " + self.name + " is " + self.color)

a = fruit("Bannana", "green")
b = fruit("Plantain", "yellow")
a = fruit("Bannana", "green")
b = fruit("Plantain", "yellow")
print(a.name, a.color)

a.name = "Orange"
a.color = "orange"

a.myfunction()
b.myfunction()'''

'''import datetime

x = datetime.datetime(2020,10,10)

print(x)'''

'''
import math
a = 345.23

print(math.floor(a))
print(math.ceil(a))'''

'''try:
    print(i)
except:
    print("There was an error here")
finally:
    print("The try except has finished")'''


sample = open("sample2.txt", "x")
sample.write(" We just appended this.")
sample.close()

sample = open("sample.txt", "r")
print(sample.read())




