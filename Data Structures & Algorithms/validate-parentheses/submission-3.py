class Solution:
    def isValid(self, s: str) -> bool:
        #create a stack
        stack = []
        hashMap = {
            ")" : "(",
            "}":"{",
            "]":"["
        }
        #iterate through the array
        for ele in s:
            if ele in hashMap:
                if stack and stack[-1] == hashMap[ele]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ele)
        #return true
        if stack:
            return False
        return True