# Importación de módulos (se realiza la ejecución del módulo importado)
# Si hay muy pocas funciones que exportar se puede usar la primera forma.
# Si no es mejor la segunda, que además da más información porque la llamada
# es del tipo functions.get_todos()
# from functions import get_todos, write_todos
import functions

while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(filepath='files/todos.txt', todos_arg=todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            print(f"{index + 1}-{item}".strip('\n'))

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number -= 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except IndexError:
            print("There is no item with that number.")
            continue
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

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
