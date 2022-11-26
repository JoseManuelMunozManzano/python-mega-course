# Modulos starndard importantes:
# shutil - 	High-level file operations, including copying.

import shutil

# nombre del archivo a crear, va a ser un zip y se va a hacer el zip con lo que hay en la carpeta files
shutil.make_archive("output", "zip", "files")
