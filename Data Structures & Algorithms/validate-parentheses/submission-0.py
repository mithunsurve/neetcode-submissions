class Solution:
    def isValid(self, s: str) -> bool:
        pMap = {
            "(":")",
            "{":"}",
            "[":"]"
        }
        stack = []
        for i in s:
            if i in pMap:
                stack.append(i)
            else:
                if stack and i == pMap[stack[-1]]:
                    stack.pop()
                else:
                    return False

        return True if not stack else False
            