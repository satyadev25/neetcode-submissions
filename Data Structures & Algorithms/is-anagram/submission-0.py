class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstCharList = list(s)
        secondCharList = list(t)
        firstCharList.sort()
        secondCharList.sort()
        return "".join(firstCharList) == "".join(secondCharList)
