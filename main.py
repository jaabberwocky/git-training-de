import os


def main():
    """
    Main function as a main entrypoint for all functions in the program.
    """
    path_list = os.listdir(os.getcwd())
    print("asdjflkasjfksdajfkdsjfkdasjfkdasjfkdasjfkasdjfkasdjfaksdjfksadfasdfjadsk")  # noqa: E501
    print(f'{path_list}')
    print(f'{add(1,2)}')


def add(x, y):
    """
    Adds two integers together.

    Args:
        x (int): First integer
        y (int): Second integer

    Returns:
        int: Result of adding x + y
    """
    result = x + y
    return result


if __name__ == "__main__":
    main()
