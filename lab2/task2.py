# Завдання 2: Генератор хешів файлів

import hashlib

def generate_file_hashes(*file_paths):
    hashes = {}
    for path in file_paths:
        try:
            with open(path, "rb") as file:
                file_data = file.read()
                file_hash = hashlib.sha256(file_data).hexdigest()
                hashes[path] = file_hash

        except FileNotFoundError:
            print(f"Error: The file '{path}' was not found.")
        except IOError:
            print(f"Error: Could not read the file '{path}'.")

    return hashes

result = generate_file_hashes("apache_logs.txt", "apache_logs2.txt", "apache_logs3.txt")

print("File hashes:")
for file_path, file_hash in result.items():
    print(f"{file_path}: {file_hash}")
