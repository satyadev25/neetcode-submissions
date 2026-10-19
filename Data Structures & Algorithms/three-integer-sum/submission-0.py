class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res_dict = {}
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(i+2, len(nums)):
        #             if nums[i] + nums[j] +nums[k] == 0:
        #                 val = [nums[i], nums[j], nums[k]]
        #                 val.sort()
        #                 key = (tuple(val))
        #                 res_dict[key] = val
        
        nums.sort()
        for i, num in enumerate(nums):
            left  = i+1
            right = len(nums)-1
            while left < right:
                total = num + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    val = [num, nums[left], nums[right]]
                    key = (tuple(val))
                    res_dict[key] = val
                    left += 1
                    right -= 1
        return list(res_dict.values())