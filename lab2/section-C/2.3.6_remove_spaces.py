
def remove_spaces(s):
    # Removes all spaces from a string.
    return s.replace(" ", "")

if(__name__ == "__main__"):
    input_string = "Hello, World! This is a test."
    print(f"Original string: '{input_string}'")
    print(f"String with spaces removed: '{remove_spaces(input_string)}'")
