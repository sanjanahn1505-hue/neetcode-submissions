from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # 1. Create order map
        order_map = {char: i for i, char in enumerate(order)}

        # 2. Check adjacent words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]

            # Find first differing char
            for j in range(min(len(w1), len(w2))):
                if w1[j]!= w2[j]:
                    if order_map[w1[j]] > order_map[w2[j]]:
                        return False
                    break # correct order for this pair
            else:
                # All chars same till min len, then longer word should come after
                # e.g. ["neetCode", "neet"] -> invalid
                if len(w1) > len(w2):
                    return False

        return True