# Python script to display file contents
def display_file_contents(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = input("Enter the source file path: ")
display_file_contents(file_path)
