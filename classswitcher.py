import os

def switch_first_character(line):
    if line.startswith('0'):
        return '1' + line[1:]
    elif line.startswith('1'):
        return '0' + line[1:]
    else:
        return line

def process_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    updated_lines = [switch_first_character(line) for line in lines]

    with open(file_path, 'w') as file:
        file.writelines(updated_lines)

def main(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory_path, filename)
            process_file(file_path)
            print(f"Processed: {filename}")

if __name__ == "__main__":
    directory_path = "test/labels" 
    main(directory_path)