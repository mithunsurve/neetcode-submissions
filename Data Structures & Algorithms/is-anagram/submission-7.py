from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hMap = defaultdict(int)
        for ele in s:
            hMap[ele] += 1

        for ele in t:
            if ele in hMap:
                if hMap[ele] == 0:
                    return False
                else:
                    hMap[ele] -= 1
            else:
                return False

        return True
