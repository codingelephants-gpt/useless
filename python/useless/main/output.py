# Version History

# 0.0.1: 23/03/2025
#     File created
#     Added emptylines function
#     Added Print function as it is a well-known function and part of outputting items to the console
#     Added testing environment
#     Added editLast function

def emptylines(n: int) -> None:
    """Prints {n} empty lines.
    Args:
        n (int): Number of empty lines
    Returns:
        None
    """
    for _ in range(n):
        print()

def Print(*objs, sep=' ', end='\n', file=None, flush=False) -> None:
    """Prints objects to the text stream file, separated by sep and followed by end.
    Args:
        *objs: Objects to print
        sep (str): Separator between objects
        end (str): End character
        file (file): File to write to
        flush (bool): Whether to flush the stream
    Returns:
        None
    """
    print(*objs, sep=sep, end=end, file=file, flush=flush)
    return None

def editLast(text: str) -> None:
    """Edits the last line of the console.
    Args:
        text (str): Text to replace the last line with
    Returns:
        None
    """

    print("\033[F\033[K", end="")
    print(text)
    return None

# Testing environment
if __name__ == "__main__":
    Print("This is", "a test")
    emptylines(3)