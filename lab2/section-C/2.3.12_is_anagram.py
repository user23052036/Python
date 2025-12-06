
def are_anagrams(s1, s2):
    """Checks if two strings are anagrams.

    Args:
        s1: The first string.
        s2: The second string.

    Returns:
        True if the strings are anagrams, False otherwise.
    """
    return sorted(s1.lower().replace(" ", "")) == sorted(s2.lower().replace(" ", ""))

if __name__ == "__main__":
    string1 = "Listen"
    string2 = "Silent"
    string3 = "Hello"
    string4 = "World"
    print(f"'{string1}' and '{string2}' are anagrams: {are_anagrams(string1, string2)}")
    print(f"'{string3}' and '{string4}' are anagrams: {are_anagrams(string3, string4)}")
