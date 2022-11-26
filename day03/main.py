todos = []

while True:
    user_action = input("Type add, show (or display) or exit: ").strip()

    # A partir de Python 3.10
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        # | bitwise OR operator
        case 'show' | 'display':
            for item in todos:
                item = item.title()
                print(item)
        case 'exit':
            break
        # default case. Se puede poner cualquier nombre de variable pero por convenio se pone _
        case _:
            print("Hey, you entered an unknown command")

print("Bye!")
