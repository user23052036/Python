
def substring_exists(s, sub):
    """Checks if a substring exists in a string.

    Args:
        s: The main string.
        sub: The substring to check for.

    Returns:
        True if the substring exists, False otherwise.
    """
    return sub in s

if __name__ == "__main__":
    main_string = "Hello, World! This is a test."
    substring1 = "World"
    substring2 = "Python"
    print(f"'{substring1}' exists in '{main_string}': {substring_exists(main_string, substring1)}")
    print(f"'{substring2}' exists in '{main_string}': {substring_exists(main_string, substring2)}")
