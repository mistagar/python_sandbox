'Count numbers from 1 - 5'
'count = 1'
'initializing our variable'

'''while count <= 5 :
    print(count)
    'count = count + 1'
    count += 1

print("My while loop is complete")
'''

'AND Logical operator'
'It is only true if both inputs are true'
'''
T & T -> T
T & F -> F
F & T -> F
F & F -> F
'''


'OR Logical Operator'
'''
T & T -> T
T & F -> T
F & T -> T
F & F -> F
'''

'NOT Logical operator'
'''
T -> F
F -> T
'''

''''GARCODE SIMPLE GUESS'
'Guess a number between 1 and 10'
count = 1
lives = 3
out_of_lives = False

print("Please guess a number between 1 and 10")
secret_number = 7
guess = int(input("Pleas enter your guess."))
while guess != secret_number and  not(out_of_lives):
    if count < lives:
        guess = int(input("Try again"))
        count += 1
    else:
        out_of_lives = True

if out_of_lives:
    print("You are out of lives. You lost.")
else:
    print("You win")
    print("Hurray! Your guess was correct")'''


'find the exponent of a number'

'''def raise_to_power(firstnumber, powernumber):
    result = 1
    for i in range(powernumber):
        result = result * firstnumber
    return result


print( raise_to_power(3,3))
'''

'''
output = open("sample.txt", "r")

for  name in  output.readlines():
    print(name)

output.close()'''

'''
output = open("sample.txt", "w")

output.write("\nKENNETH")

output.close()
'''

class dog:
    def __init__(self, name, color):
        self.dogname = name
        self.dogcolor = color

    def show(self):
        print("Hello my name is "+ self.dogname + " and my color is " + self.dogcolor)

samuels_dog = dog("Bingo", "Brown")
samuels_dog.show()

endurance_dog = dog("Champion", "Grey")
endurance_dog.show()

shaloms_dog = dog("Murphy", "Black")
shaloms_dog.show()





