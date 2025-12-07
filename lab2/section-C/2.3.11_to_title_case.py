
def to_title_case(s):
    # Turning the first letter of each word capital

    title_cased_s = ""
    new_word = True

    for char in s:
        if new_word and 'a' <= char <= 'z':
            title_cased_s += chr(ord(char) - 32)
            new_word = False
        elif char == ' ':
            title_cased_s += char
            new_word = True
        else:
            title_cased_s += char
            new_word = False

    return title_cased_s

if(__name__ == "__main__"):
    input_string = "hello world, this is a test."
    print(f"Original string: '{input_string}'")
    print(f"Title cased string: '{to_title_case(input_string)}'")
