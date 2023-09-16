'''class Car:
    name = ""
    gear = 0


car1 = Car()
car2 = Car()
car3 = Car()

car1.name = "toyota"
car2.name ="Benz"
car3.name = "Ferrari"

car1.gear = 5
car2.gear = 4
car3.gear = 7

print("Car2 is a " + car2.name)
'''

'''class Car:
    def __init__(self, name, gear):
        self.name = name
        self.gear = gear

car1 = Car("Toyota", 5)

print("Car1's name is " + car1.name)
'''

'''class employee:
    def __init__(self, firstname, lastname, dept, level, salary):
        self.fname = firstname
        self.lname = lastname
        self.dept = dept
        self.level = level
        self.salary = salary

admin = employee("Endurance", "Isibor", "Accounts", "12", 150000)
secretary = employee("Tamara", "Jackson", )
print(f" The admins name is {admin.fname} {admin.lname} and he works in "
      f" {admin.dept} on level {admin.level}  and he is paid {admin.salary}")
'''

def calculate_vat(percentage, price):
    vat = (percentage/100) * price
    new_price = vat + price
    return new_price

oraimo_price = calculate_vat(7.5, 8000)
print(oraimo_price)





