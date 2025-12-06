
def count_words(s):
    # Counts the number of words in a string.
    return len(s.split())

if(__name__ == "__main__"):
    input_string = "Hello, World! This is a test."
    print(f"Number of words in '{input_string}': {count_words(input_string)}")
