# 451. Sort Characters By Frequency

"""
Input: s = "tree"
Output: "eert"

Input: s = "cccaaa"
Output: "aaaccc"

Input: s = "Aabb"
Output: "bbAa"
"""

class Solution:
    def frequencySort(self, s: str) -> str:
        my_dict = {}
        for ch in s:
            my_dict[ch] = my_dict.get(ch,"") + ch
        
        # by default sorted returns list of tupils
        sorted_dict = dict(sorted(my_dict.items(), key = lambda x:len(x[1]), reverse = True))

        return ''.join(sorted_dict.values())


# my_dict.items()
#         │
#         ▼
# dict_items
#         │
#    sorted(...)
#         │
#         ▼
#        list
#         │
#         ├── ('a', 'aaa')   ← tuple
#         ├── ('b', 'bbbbb') ← tuple
#         └── ('c', 'x')     ← tuple