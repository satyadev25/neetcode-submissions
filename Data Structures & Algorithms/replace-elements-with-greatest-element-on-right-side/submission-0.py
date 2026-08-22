class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest_value_seen = 0
        for i in range(len(arr)-1):
            grNum = 0
            for j in range(i+1, len(arr)):
                if grNum < arr[j]:
                    grNum = arr[j]
            arr[i] = grNum
        arr[len(arr)-1] = -1
        return arr
                    