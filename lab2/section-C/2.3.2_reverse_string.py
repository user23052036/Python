
def reverse_string(s):
    # Reverses a string without using slicing.
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

if(__name__ == "__main__"):
    input_string = "Hello, World!"
    print(f"Original string: {input_string}")
    print(f"Reversed string: {reverse_string(input_string)}")
