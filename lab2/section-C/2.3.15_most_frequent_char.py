
from collections import Counter

# Finds the most frequent character in a string.
def most_frequent_char(s):
    if not s:
        return None

    s = s.replace(" ", "").lower()
    if not s:
        return None # if no valid input present return None

    freq = {}  # dictionary to count characters

    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    most_common = None
    highest = 0

    for ch, count in freq.items():
        if count > highest:
            highest = count
            most_common = ch

    return most_common


if(__name__ == "__main__"):
    input_string = "programming is fun"
    print(f"The most frequent character in '{input_string}' is: '{most_frequent_char(input_string)}'")
