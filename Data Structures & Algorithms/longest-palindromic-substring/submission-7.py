class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n<2:
            return s
        result = ""
        for i in range(n):
            r, l = i, i-1
            while r<n and l>=0 and s[l]==s[r]:
                if (r-l+1)>len(result):
                    result = s[l:r+1]
                l-=1
                r+=1
            r, l = i, i
            while r<n and l>=0 and s[l]==s[r]:
                if (r-l+1)>len(result):
                    result = s[l:r+1]
                l-=1
                r+=1

        return result

