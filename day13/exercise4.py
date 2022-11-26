# Write a program that gets a list of names from the user and returns the number of names given.
# You are encouraged to use a function. Here is how the program would work:
#
# Enter names separated by commas (no spaces): john,jay,marry
# 3
def get_number_of_names(names_list_local):
    return len(names_list_local)


names = input("Enter names separated by commas (no spaces): ")
names_list = names.split(",")
number_names = get_number_of_names(names_list)
print(number_names)
