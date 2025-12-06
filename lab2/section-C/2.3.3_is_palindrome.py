
def is_palindrome(s):
    # Checks if a string is a palindrome.

    s = s.lower().replace(" ", "")
    return s == s[::-1]

if(__name__ == "__main__"):
    pal_str = "A man a plan a canal Panama"
    non_pal_str = "Hello, World!"
    print(f"'{pal_string}' is a palindrome: {is_palindrome(pal_str)}")
    print(f"'{non_pal_str}' is a palindrome: {is_palindrome(non_pal_str)}")
