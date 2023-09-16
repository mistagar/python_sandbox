import time
import random
import turtle
import test


tt = test.greet()

print(tt)
#epoch 1970 jan 1st

t = turtle.Pen()
t.color(0,1,0)
t.begin_fill()
for i in range(1,9):
    t.forward(50)
    t.left(45)

t.right(90)
t.up()

t.forward(50)
time.sleep(2)
t.down()
for i in range(1,9):
    t.forward(50)
    t.left(45)
t.end_fill()




time.sleep(5)


'''
lucky_number = random.randint(1,10)
while lucky_number != guess:
    guess = int(input("Try again. Guess a number between 1 and 10"))

print("Good job. you got it.")'''

'''while True:
    guess = int(input("Please guess a number between 1 and 10"))

    if guess == lucky_number:
        print("Good job")
        break
'''









'''test = str(random.randint(1000000,9999999))

print("080"+test)
fruits = ["apple", "pineapple", "watermelon","mango", "orange"]
favourite = random.choice(fruits)
print(fruits)

random.shuffle(fruits)
print(fruits)
print(favourite)
'''



