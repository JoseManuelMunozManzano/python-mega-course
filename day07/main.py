while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    match user_action:
        case 'add':
            # El \n es para escribir en todos.txt en distintas líneas
            todo = input("Enter a todo: ") + "\n"

            # Path relativo al directorio root del proyecto
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('files/todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            # Eliminando \n de la lista con list comprehensions
            # new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                # Eliminando \n directamente en nuestro for
                item = item.strip('\n')
                print(f"{index + 1}-{item}")
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            new_todo = input("Enter new todo: ")
            todos[number - 1] = new_todo
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
        case 'exit':
            break

print("Bye!")
