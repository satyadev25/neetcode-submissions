class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            st = "".join(sorted(s)).lower()
            result[st].append(s)
        
        return list(result.values())

