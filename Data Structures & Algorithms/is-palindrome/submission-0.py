class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for i in range(len(s)):
            if s[i].isalnum():
                new_str += s[i]
        left = 0
        new_str = new_str.lower().strip()

        right = len(new_str)-1
        print(new_str)
        while left < right:
            if new_str[left] != new_str[right]:
                return False
            left += 1
            right -= 1
        return True