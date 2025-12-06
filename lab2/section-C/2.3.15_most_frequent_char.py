
from collections import Counter

def most_frequent_char(s):
    """Finds the most frequent character in a string.

    Args:
        s: The input string.

    Returns:
        The most frequent character in the string.
    """
    if not s:
        return None
    # Remove spaces and convert to lowercase for accurate counting
    s = s.replace(" ", "").lower()
    if not s:
        return None
    return Counter(s).most_common(1)[0][0]

if __name__ == "__main__":
    input_string = "programming is fun"
    print(f"The most frequent character in '{input_string}' is: '{most_frequent_char(input_string)}'")
