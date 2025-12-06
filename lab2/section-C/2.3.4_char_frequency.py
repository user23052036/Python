
def char_frequency(s):
    # Counts the frequency of each character in a string.

    frequency = {}
    for char in s:
        if(char in frequency): frequency[char] += 1
        else: frequency[char] = 1
    return frequency

if(__name__ == "__main__"):
    input_string = "hello world"
    print(f"Character frequency in '{input_string}': {char_frequency(input_string)}")
