while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    if 'add' in user_action:
        # Se llama list slicing y sirve para extraer parte de un string
        # Si se informa de esta forma [4:8] coge desde el carácter 4 incluido hasta el 8 no incluido
        todo = user_action[4:]

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}-{item}")

    elif 'edit' in user_action:
        number = int(user_action[5:])
        number -= 1

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + '\n'

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'complete' in user_action:
        number = int(user_action[9:])

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        index = number - 1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"Todo {todo_to_remove} was removed from the list"
        print(message)

    elif 'exit' in user_action:
        break

    else:
        print("Command is not valid.")

print("Bye!")
