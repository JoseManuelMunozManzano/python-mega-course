# parameter
def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


# Función que funciona como un Procedure. No devuelve nada
def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        # argument. Se puede indicar el nombre del argumento, pero no es obligatorio
        # Hacer lo que haga el código más fácil de leer
        todos = get_todos(filepath='files/todos.txt')

        todos.append(todo + '\n')

        write_todos(filepath='files/todos.txt', todos_arg=todos)

    elif user_action.startswith('show'):
        todos = get_todos('files/todos.txt')

        for index, item in enumerate(todos):
            print(f"{index + 1}-{item}".strip('\n'))

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number -= 1

            todos = get_todos('files/todos.txt')

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos('files/todos.txt', todos)
        except IndexError:
            print("There is no item with that number.")
            continue
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos('files/todos.txt')

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos('files/todos.txt', todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Command is not valid.")

print("Bye!")
