class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unqIntSet = set()
        for i, j in enumerate(nums):
            if j in unqIntSet:
                return True
            else:
                unqIntSet.add(j)

        return False