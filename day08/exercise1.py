# A client wants to buy a coin-flip probability program from you.
# The programs should work like this:
# 1. The user runs the program. The program asks the user to enter "head" or "tail".
# The user flips a coin on their desk, table, floor, etc., and then enters "head" or "tail".
# The user does the same over and over again.

# Throw the coin and enter head or tail here: ? head
# 100.0
# Throw the coin and enter head or tail here: ? tail
# 50.0
# Throw the coin and enter head or tail here: ? head
# 66.666666666666
# Throw the coin and enter head or tail here: ? head
# 75.0
# Throw the coin and enter head or tail here: ?

# In each cycle, the program should return the current percentage of heads in the program.
# Try using a with-context manager in your code.
while True:
    result = input("Throw the coin and enter head or tail here: ? ").strip()

    match result:
        case 'exit':
            break
        case 'head' | 'tail':
            with open("files/coin.txt", "r") as file:
                results = file.readlines()

            results.append(result + '\n')

            with open("files/coin.txt", "w") as file:
                file.writelines(results)

            heads = results.count("head\n")
            print(heads/len(results) * 100)
        case _:
            print("Please enter head or tail")
