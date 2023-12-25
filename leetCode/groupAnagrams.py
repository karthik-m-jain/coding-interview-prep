"""
Question:

    49. Given an array of strings strs, group the anagrams together. You can return the answer in any order.
        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

    Example 1:

    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    
    Example 2:

    Input: strs = [""]
    Output: [[""]]
    
    Example 3:

    Input: strs = ["a"]
    Output: [["a"]]
"""

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #for any key not already present in the dictionary, the default value should be an empty list ([]).
        result = defaultdict(list)

        for i in strs:
            count = [0] * 26
            for j in i:
                count[ord(j) - ord('a')] += 1
            
            result[tuple(count)].append(i)
        
        return result.values()

solution = Solution()

print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(solution.groupAnagrams([""]))

"""
    Time-complexity = O(m*n) -> m is size of list, n is size of each string
    Space-complexity = O(m)

    Alternative solutions:
"""