class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum = []
        rightsum = [0]*len(nums)

        left = 0
        for num in nums:
            left += num
            leftsum.append(left)
        
        right = 0
        for i in range(len(nums) - 1, -1, -1):
            right += nums[i]
            rightsum[i] += right

        for i in range(len(nums)):
            if leftsum[i] == rightsum[i]:
                return i
        return -1


    