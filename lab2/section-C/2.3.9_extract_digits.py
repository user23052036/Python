
def extract_digits(s):
    # Extracts all digits from a string.
    digits = ""
    for char in s:
        if char.isdigit():
            digits += char
    return digits

if(__name__ == "__main__"):
    input_string = "abc123def456ghi"
    print(f"Original string: {input_string}")
    print(f"Extracted digits: {extract_digits(input_string)}")
