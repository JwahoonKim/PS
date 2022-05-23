import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [ w for w in re.sub('[!?\',;.]', ' ', paragraph).lower().split() if w not in banned ]
        counts = Counter(words)
        return counts.most_common(1)[0][0]