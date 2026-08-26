from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # num -> index

        for i, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need], i] # smaller index first
            seen[num] = i