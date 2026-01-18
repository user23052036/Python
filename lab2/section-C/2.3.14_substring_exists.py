
def substring_exists(s, sub):
    # Check whether 'sub' exists inside 's'
    # Loop through the main string
    for i in range(len(s) - len(sub)+1):
        # Compare the slice with the substring
        if(s[i:i+len(sub)] == sub):
            return True

    return False


if(__name__ == "__main__"):
    main_string = "Hello, World! This is a test."
    substring1 = "World"
    substring2 = "Python"
    print(f"'{substring1}' exists in '{main_string}': {substring_exists(main_string, substring1)}")
    print(f"'{substring2}' exists in '{main_string}': {substring_exists(main_string, substring2)}")
