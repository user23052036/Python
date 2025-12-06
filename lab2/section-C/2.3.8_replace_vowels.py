
def replace_vowels(s):
    # Replaces all vowels in a string with '*'.
    vowels = "aeiouAEIOU"
    for vowel in vowels:
        s = s.replace(vowel, "*")
    return s

if(__name__ == "__main__"):
    input_string = "Hello, World!"
    print(f"Original string: {input_string}")
    print(f"String with vowels replaced: {replace_vowels(input_string)}")
