class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixsums = []
        total = 0
        for num in nums:
            total += num
            self.prefixsums.append(total)

    def sumRange(self, left: int, right: int) -> int:
        presumright = self.prefixsums[right]
        presumleft = self.prefixsums[left -1] if left > 0 else 0
        return presumright - presumleft
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)