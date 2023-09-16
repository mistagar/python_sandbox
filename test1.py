
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    count = 1
    match user_action:
        case "add":
            todo = input("Enter a todo action:") + "\n"
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()

        case "show":
            # for index, item in enumerate(todos):
            #
            #     print(index,item)
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()


            for index, item in enumerate(todos):
                print(f"{index + 1}- {item}")

        case "edit":
            number = int(input("Enter the number of the todo you want to edit:"))
            number = number - 1
            todos[number] = input("Edit your todo")
            print("Update Succesfull")
        case "complete":
            number = int(input("Enter the number of hte todo you have completed:"))
            number = number-1
            todos.pop(number)
        case "exit":
            break

print("Bye!")
