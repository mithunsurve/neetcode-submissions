class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {
            "}":"{",
            "]":"[",
            ")":"("
        }
        stack = []

        for ele in s:
            if ele not in hashMap:
                stack.append(ele)
            else:
                if stack and stack[-1] == hashMap[ele]:
                    stack.pop()
                else:
                    return False

        return True if not stack else False