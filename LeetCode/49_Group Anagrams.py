from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for str in strs:
            sorted_str = ''.join(sorted(str))
            anagrams[sorted_str].append(str)

        return anagrams.values()