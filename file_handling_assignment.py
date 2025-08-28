"""
📝 File Handling & Error Handling Assignment
Author: Oluwalayomi Jesuloluwa

This program demonstrates:
1. Reading a file and writing a modified version to a new file.
2. Handling errors when the file does not exist or cannot be read.
"""

def modify_file(input_file, output_file):
    """
    Reads content from input_file, modifies it, and writes to output_file.
    Modification: Converts all text to uppercase.
    """
    try:
        with open(input_file, "r") as file:
            content = file.read()

        # Example modification: convert text to uppercase
        modified_content = content.upper()

        with open(output_file, "w") as file:
            file.write(modified_content)

        print(f"✅ Modified file saved as '{output_file}'")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_file}' was not found.")
    except IOError:
        print(f"❌ Error: Could not read or write file '{input_file}'.")


# --- Main program ---
filename = input("Enter the name of the file to read: ")
output_filename = "modified_" + filename

modify_file(filename, output_filename)
