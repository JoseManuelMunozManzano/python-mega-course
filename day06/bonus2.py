# Cada elemento de contents irá a un fichero
contents = ["All carrots are to be sliced longitudinally.",
            "The carrots were reportedly sliced.",
            "The slicing process was well presented."]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

# Siendo
# a = [1, 2, 3]
# b = [10, 20, 30]
# list(zip(a, b)) devuelve [(1, 10), (2, 20), (3, 30)]
for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", 'w')
    file.write(content)
    