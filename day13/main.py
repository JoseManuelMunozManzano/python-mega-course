# default parameter
# docstring se escriben en la primera línea usando triples comillas. Se recomienda poner siempre un docstring.
def get_todos(filepath='files/todos.txt'):
    """ Read a text file and return the list of
        to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


# Obtener el docstring
print(help(get_todos))


# default parameters siempre van al final
def write_todos(todos_arg, filepath='files/todos.txt'):
    """ Write the to-do items list in the text file. """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        # No hace falta respetar el orden si se indica el nombre del parámetro
        write_todos(filepath='files/todos.txt', todos_arg=todos)

    elif user_action.startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos):
            print(f"{index + 1}-{item}".strip('\n'))

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number -= 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)
        except IndexError:
            print("There is no item with that number.")
            continue
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

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
