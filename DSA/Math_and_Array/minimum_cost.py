# You are given a string S consisting of lowercase English letters ('a'–'z').

"""
Your task is to convert all characters in the string into a single lowercase English letter such 
that the total conversion cost is minimized.

The cost of converting a character c to a character t is defined as follows:
If both c and t are vowels (a, e, i, o, u) or both are consonants, the cost is:

∣ASCII(c) − ASCII(t)∣

If one is a vowel and the other is a consonant, the cost is 10.
Return the minimum total cost required to make all characters in the string identical.

Input
A single string S containing only lowercase English letters.

Output
An integer representing the minimum total conversion cost.
"""

def minimum_cost(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}

    ans = float('inf')

    # Try every lowercase letter as the final target
    for target in map(chr, range(ord('a'), ord('z')+1)):    # smart
        total = 0

        for ch in s:
            if (ch in vowels) == (target in vowels):
                # Same group
                total += abs(ord(ch) - ord(target))
            else:
                # Different groups
                total += 10

        ans = min(ans, total)

    return ans


# Example
s = input().strip()
print(minimum_cost(s))