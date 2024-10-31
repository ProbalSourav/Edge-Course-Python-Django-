class FileManager:
    def __init__(self, filename):
        self.filename = filename  # Store filename during initialization

    def write_to_file(self, content):
        # Write content to file in write mode
        file = open(self.filename, 'w')
        try:
            file.write(content)
        finally:
            file.close()  # Ensure the file is closed after writing

    def read_from_file(self):
        try:
            # Read content from file if it exists
            file = open(self.filename, 'r')
            try:
                return file.read()
            finally:
                file.close()  # Ensure the file is closed after reading
        except FileNotFoundError:
            # Handle case when file is not found by creating an empty file
            print(f"File '{self.filename}' not found. Creating the file.")
            with open(self.filename, 'w'):
                pass
            return ""

def main():
    # Specify the file name to be used
    filename = 'user_input.txt'
    file_manager = FileManager(filename)

    # Ask for user input to write to the file
    user_input = input("Enter some text to write to the file: ")
    file_manager.write_to_file(user_input)

    # Read and display content from the file
    print("Reading from the file:")
    content = file_manager.read_from_file()
    print(content)

if __name__ == "__main__":
    main()
