def file_finder(dirs, file_name, current_path=""):
    # Check if the current node is a tuple (directory)
    if isinstance(dirs, tuple):
        # Extract the directory name and its contents
        dir_name, contents = dirs

        # Create the current path by joining the current path with the directory name
        current_path = current_path + dir_name + "/"

        # Recursively search in the contents of the directory
        for item in contents:
            result = file_finder(item, file_name, current_path)

            # If the file is found, return the full path
            if result:
                return result

    # Check if the current node is a string (file)
    elif isinstance(dirs, str) and dirs == file_name:
        return current_path + file_name

    # File not found in this branch
    return None

# Example usage:
dirs = ("home", [
    ("Documents", [
        ("FP", ["lists.txt", "recursion.pdf", "functions.ipynb"]),
        ("Python", ["hello_world.py", "readme.md"])
    ]),
    ("Downloads", [
        ("Movies", [
            ("TV Series", ["BreakingBad.mp4", "TheBigBangTheory.avi"]),
            "1.avi", "22", "001.mp4"
        ])
    ]),
    "tmp.txt", "page.html"
])

print(file_finder(dirs, 'Documents'))        # Output: None (Documents is a sub-directory, not a file)
print(file_finder(dirs, 'recursion.pdf'))     # Output: "home/Documents/FP/recursion.pdf"
print(file_finder(dirs, 'hello_world.py'))    # Output: "home/Documents/Python/hello_world.py"
print(file_finder(dirs, '22'))               # Output: "home/Downloads/Movies/22"
