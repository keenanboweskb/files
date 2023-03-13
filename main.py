__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

from zipfile import ZipFile
import os

files_list = []

# Question 1


def clean_cache():
    directory = "files/cache"

    if os.path.isdir(directory):
        for files in os.listdir(directory):
            os.remove(os.path.join(directory, files))
    else:
        os.mkdir(directory)
    return directory

# Question 2


def cache_zip(zip_file, cache_dir):

    with ZipFile(zip_file, 'r') as zip:
        zip.extractall(cache_dir)
    return zip_file

# Question 3


def cached_files():
    path = f"{os.getcwd()}/files/cache"
    files = os.listdir(path)

    for f in files:
        abs_files = os.path.abspath(path)
        files_list.append(f'{abs_files}/{f}')
    return files_list

# Question 4


def find_password(list_of_file_paths):
    word = "password"

    for file in list_of_file_paths:
        with open(file, 'r') as data:
            for line_number, line in enumerate(data, start=1):
                if word in line:
                    print(line)
                    break
    return line


clean_cache()
cache_zip("files/data.zip", "files/cache")
print(cached_files())
find_password(files_list)
