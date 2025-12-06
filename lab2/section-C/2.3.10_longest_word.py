
def manual_split(sentence):
    words = []
    current = ""

    for ch in sentence:
        if ch != " ":
            current += ch
        else:
             # avoids multiple spaces between , start and end of sentence so 
            if current != "": # that it would not push meaningless words like "" into the lists    
                words.append(current)
                current = ""

    if current != "":
        words.append(current)

    return words


def longest_word(sentence):
    words = manual_split(sentence)
     # words = sentence.split()   # break the sentence into separate words and stores in list

    longest = ""
    for w in words:
        if len(w) > len(longest):
            longest = w

    return longest     


if(__name__ == "__main__"):
    input_sentence = "Find the longest word in this sentence."
    print(f"Sentence: '{input_sentence}'")
    print(f"Longest word: '{longest_word(input_sentence)}'")

