import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    # Para extraer un zip sera 'r', pero para generar un zip es 'w'
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


if __name__ == '__main__':
    make_archive(filepaths=['bonus_files/a.txt', 'bonus_files/c.txt'], dest_dir='bonus_files')
