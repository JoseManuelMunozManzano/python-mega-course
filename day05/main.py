todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            # enumerate() permite acceder a los items de la lista y a sus índices
            for index, item in enumerate(todos):
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
