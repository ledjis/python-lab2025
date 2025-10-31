# Завдання 1: Аналізатор лог-файлів

import re

def analyze_log_file(log_file_path):
    result = {}  # dictionary to store counts of HTTP status codes
    pattern = re.compile(r'"\s(\d{3})\s')  # regex to find three digits after a quote and space

    try:
        with open(log_file_path, "r", encoding="utf-8") as file:
            for line in file:
                match = pattern.search(line)
                if match:
                    code = match.group(1)
                    if code in result:
                        result[code] += 1
                    else:
                        result[code] = 1

    except FileNotFoundError:
        print(f"Error: The file '{log_file_path}' was not found.")
    except IOError:
        print(f"Error: Could not read the file '{log_file_path}'.")
    return result

file_path = "apache_logs.txt"
codes_count = analyze_log_file(file_path)
print("HTTP response codes count:")
for code, count in codes_count.items():
    print(f"{code}: {count}")

