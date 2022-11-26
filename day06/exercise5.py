# create a program that reads a.txt, b.txt and c.txt files and prints out the content of each in the command line.
# The expected output would be like the following:
# I am a.
# I am b.
# I am c.
filenames = ["a.txt", "b.txt", "c.txt"]
for filename in filenames:
    file = open(f"files/{filename}", 'r')
    content = file.read()
    file.close()
    print(content)
