# Create a program that reads the file essay.txt and prints out its text.
# The first letter of each word in the output should be uppercase.
file = open("files/essay.txt", 'r')
content = file.read()
print(content.title())
file.close()