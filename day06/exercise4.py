# Create a program that generates multiple text files by iterating over the filenames list.
# The text Hello should be written inside each generated text file.

filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:
    file = open(f"files/{filename}", 'w')
    file.write("Hello")
    file.close()