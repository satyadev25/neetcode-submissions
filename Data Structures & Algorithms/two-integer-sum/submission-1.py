class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        already_seen = {}
        for i, val in enumerate(nums):
            j = target - val
            if j in already_seen:
                return [already_seen[j], i]
            else:
                already_seen[val] = i

        return []

