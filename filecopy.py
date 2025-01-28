# Python script to copy file contents from one file to another
def copy_file_contents(source_file, destination_file):
    try:
        with open(source_file, 'r') as src_file:
            content = src_file.read()

        with open(destination_file, 'w') as dest_file:
            dest_file.write(content)

        print(f"Contents successfully copied from '{source_file}' to '{destination_file}'.")
    except FileNotFoundError:
        print(f"Error: The file '{source_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

source_file = input("Enter the source file path: ")
destination_file = input("Enter the destination file path: ")
copy_file_contents(source_file, destination_file)
