import os

def CleanFiles(files):
    for file in files:
        if os.path.exists(file):
            os.remove(file)
            # Create the file
            with open(file, 'w') as new_file:
                print(f"The file '{file}' has been created.")
        else:
            # Create the file
            with open(file, 'w') as new_file:
                print(f"The file '{file}' has been created.")


def DeleteFiles(files):
    for file in files:
        if os.path.exists(file):
            os.remove(file)