class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res_dict = {}
        for i, num in enumerate(nums):
            if num in res_dict:
                return [res_dict[num], i]
            else:
                diff = target - num
                res_dict[diff] = i

        return []

