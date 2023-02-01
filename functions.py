FILEPATH = "todo.txt"


def read_todo(filepath=FILEPATH):
    """Read a text file and return the list of
    to-do items"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todo(todos_arg, filepath=FILEPATH):
    """Write the todo items list in the next file"""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")

