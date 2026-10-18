class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        count = 0
        presum = {0:1}
        curSum = 0
        
        for i in range(len(nums)):
            curSum += nums[i]
            diff = curSum - k
            count += presum.get(diff, 0)
            presum[curSum] = presum.get(curSum, 0)+1
        return count

