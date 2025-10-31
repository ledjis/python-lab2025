# Завдання 3: Фільтрація IP-адрес з файлу

def filter_ips(input_file_path, output_file_path, allowed_ips):
    ip_counts = {ip: 0 for ip in allowed_ips}

    try:
        with open(input_file_path, "r", encoding="utf-8") as infile:
            for line in infile:
                parts = line.split()
                if len(parts) > 0:
                    ip = parts[0]
                    if ip in allowed_ips:
                        if ip in ip_counts:
                            ip_counts[ip] += 1
                        else:
                            ip_counts[ip] = 1

        with open(output_file_path, "w", encoding="utf-8") as outfile:
            for ip, count in ip_counts.items():
                outfile.write(f"{ip} - {count}\n")

        print(f"Results have been saved to '{output_file_path}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")
    except IOError:
        print(f"Error: Could not read or write to file.")

allowed_ips = ["83.149.9.216", "192.168.1.10", "10.0.0.5", "24.236.252.67", "66.249.73.135"]
filter_ips("apache_logs.txt", "filtered_ips.txt", allowed_ips)
