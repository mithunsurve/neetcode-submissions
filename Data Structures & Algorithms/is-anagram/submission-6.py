class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        ele = {}
        for i in s:
            if i in ele:
                ele[i] +=1
            else:
                ele[i]=1
        print(ele)
                
        for i in t:
            if i in ele:
                ele[i] -=1
                if ele[i] < 0:
                    return False
            else:
                return False
        return True

