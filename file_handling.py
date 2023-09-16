#
# my_text = open("C:\Users\hp\OneDrive\Documents\GARCODE\sample.txt", "r")
# print(my_text.read())

print("Welcome to Our GPA Calculator")
num_of_courses = int(input("Please how many courses did you offer?"))

total_wp = 0
total_gu = 0


while(num_of_courses != 0):
    course_title = input("Enter course title")
    score = int(input("What did you score in this course?"))
    course_unit = int(input("Enter your course unit")) #note that weight point is the course unit

    num_of_courses = num_of_courses - 1


    if score >= 70 and score <= 100:
        grade = "A"
        grade_unit = 5

    elif score >= 60 and score <= 69:
        grade = "B"
        grade_unit = 4
    elif score >= 50 and score <= 59:
        grade = "C"
        grade_unit = 3
    elif score >= 45 and score <= 49:
        grade = "D"
        grade_unit = 2
    elif score >= 40 and score <= 44:
        grade = "E"
        grade_unit = 1
    elif score >= 0 and score <= 39:
        grade = "F"
        grade_unit = 0
    else:
        print("You entered the invalid score")

    wp = course_unit * grade_unit
    total_wp = total_wp + wp
    total_gu = total_gu + grade_unit

gpa = str(total_wp / total_gu)
print("Your GPA is  = " + gpa)



