# 49. Group Anagrams

"""
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]

Input: strs = ["a"]
Output: [["a"]]
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        my_dict = {}
        for word in strs:
            sorted_word = tuple(sorted(word))

            if sorted_word in my_dict:
                my_dict[sorted_word].append(word)
            else:
                my_dict[sorted_word] = word

        answers = []
        for val in my_dict.values():
            answers.append(val)
        return answers
    

class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in my_dict:
                my_dict[key] = []
            my_dict[key].append(word)
        return list(my_dict.values())
    

from collections import defaultdict
class Solution3:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        # No if statement is needed because defaultdict(list) automatically creates an empty list for new keys.
        for word in strs:
            key = "".join(sorted(word))
            my_dict[key].append(word)

        return list(my_dict.values())