
def to_uppercase(s):
    # Converts a string to uppercase without using built-in function.

    uppercase_s = ""
    for char in s:
        if 'a' <= char <= 'z':
            uppercase_s += chr(ord(char) - 32)
        else:
            uppercase_s += char
    return uppercase_s

if(__name__ == "__main__"):
    input_string = "Hello, World!"
    print(f"Original string: {input_string}")
    print(f"Uppercase string: {to_uppercase(input_string)}")


# ascii -> char      chr()
# char -> ascii      ord()
