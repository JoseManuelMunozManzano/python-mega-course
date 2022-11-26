# Please place the ips list in a .py file:
#
# ips = ['100.122.133.105', '100.122.133.111']
#
# Your task is to create a program that lets the user enter an index and the program returns
# the IP address with that index.
#
# Here is how the program would behave when executed:
# Enter the index of the IP you want: 1
# You chose 100.122.133.111
ips = ['100.122.133.105', '100.122.133.111']
indexIp = int(input('Enter the index of the IP you want: '));
print(f"You chose {ips[indexIp]}")
