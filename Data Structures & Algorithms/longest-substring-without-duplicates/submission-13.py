class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hMap = {}
        left=0
        result=0
        for right in range(len(s)):
            if s[right] in hMap:
                left = max(hMap[s[right]] + 1, left)
            hMap[s[right]]=right
            result=max(right-left+1, result)

        return result


                