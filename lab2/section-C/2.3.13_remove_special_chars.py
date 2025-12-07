
# removing special charecters from a string
def remove_special_chars(s):
    result = ""
    for char in s:
        if char.isalnum() or char.isspace():
            result += char
    return result


if(__name__ == "__main__"):
    input_string = "Hello, World! This is a test with @#$ special characters."
    print(f"Original string: '{input_string}'")
    print(f"String with special characters removed: '{remove_special_chars(input_string)}'")
