
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print("Reading file content :")
            for line_number, line in enumerate(file, start=1):
                print(f"Line {line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")


# Calling the function
read_file("sample.txt")
