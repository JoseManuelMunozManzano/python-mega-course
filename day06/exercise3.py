# With the members.txt file
# Create a program that, whenever executed, asks the user to enter a new member in the command line:
#   Add a new member: Solomon Right
#
# Then, the member is added to members.txt. In this case, the text file content would be:
# John Smith
#
# Sen Lakmi
#
# Sono Octonot
#
# Solomon Right

while True:
    member = input("Add a new member: ")
    if member == 'exit':
        break

    file = open("files/members.txt", 'r')
    members = file.readlines()
    file.close()

    members.append(member + '\n')

    file = open("files/members.txt", 'w')
    file.writelines(members)
    file.close()