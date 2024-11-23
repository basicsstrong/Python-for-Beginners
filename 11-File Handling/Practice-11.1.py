def read_file():
    try:
        # To open a file, provide the file name (if it's in the same directory)
        # Example: with open("data.txt", "r") as file:
        
        # If the file is located in a different directory, provide the full path
        # Example: with open("/path/to/your/file/data.txt", "r") as file:
        
        # If you are using relative paths, make sure to include the correct relative path
        # Example: if the file is in a subdirectory called "files":
        # with open("files/data.txt", "r") as file:
        
        # Try to open the file and read its contents
        with open("data.txt", "r") as file:  # Modify "data.txt" with the correct path if necessary
            content = file.read()
            print("File content:")
            print(content)
    
    except FileNotFoundError:
        # If the file is not found, catch the error and display a message
        print("File not found! Please check the file name.")

# Example usage
if __name__ == "__main__":
    read_file()
