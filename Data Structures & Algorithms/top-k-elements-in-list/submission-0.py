class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first SolDefaultDict, ution
        # freqCount = defaultdict(int)
        # for i in nums:
        #     freqCount[i] += 1
        
        # # get the freq arr
        # sorted_list = sorted(freqCount, key = lambda x :freqCount[x], reverse=True)
        # return sorted_list[:k]

        freq_map = defaultdict(int)
        for i in nums:
            freq_map[i] += 1

        arr = [[] for _ in range(len(nums)+1)]
        for num, freq in freq_map.items():
            arr[freq].append(num)

        res = []
        for i in range(len(arr)-1, 0, -1):
            for num in arr[i]:
                res.append(num)
                if len(res) == k:
                    return res

        return res

