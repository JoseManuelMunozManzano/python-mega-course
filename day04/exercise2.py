# Please have a look at the list below:
# ranking = ['John', 'Sen', 'Marry']
# The list indicates that John won 1st place, while Sen got 2nd and Marry the 3rd.
# Users want to know who got what place, so create a program that contains the list above.
# The program lets the user enter a rank number and returns the person who has that rank.
# Here is how the program would behave:
# Enter rank number: 2
# Sen

ranking = ['John', 'Sen', 'Marry']
rank = int(input("Enter rank number: "))
print(ranking[rank - 1])
