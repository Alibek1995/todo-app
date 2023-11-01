FILEPATH = 'todos.txt'

def get_todos(path=FILEPATH):
    """ Read text file and return the of list of
    todo items
    """
    with open(path, 'r') as file_local:
        todos_local = file_local.readlines()

    return todos_local


def write_todos(todos_arg, path=FILEPATH):
    """ Write todo item list to the file

    """
    with open(path, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("hello")
    print(get_todos())
