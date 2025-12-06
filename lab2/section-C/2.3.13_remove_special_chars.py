
import re

def remove_special_chars(s):
    """Removes special characters from a string.

    Args:
        s: The input string.

    Returns:
        The string with special characters removed.
    """
    return re.sub(r'[^a-zA-Z0-9\s]', '', s)

if __name__ == "__main__":
    input_string = "Hello, World! This is a test with @#$ special characters."
    print(f"Original string: '{input_string}'")
    print(f"String with special characters removed: '{remove_special_chars(input_string)}'")
