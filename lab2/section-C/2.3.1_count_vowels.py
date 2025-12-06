
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

if(__name__ == "__main__"):
    input_string = "Hello, World!"
    print(f"Number of vowels in '{input_string}': {count_vowels(input_string)}")
