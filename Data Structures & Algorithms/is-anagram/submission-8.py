from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #create a dictonary
        count = {}
        #go through the first string & add the character count to the dict
        for char in s:
            if char in count:
                count[char]+=1
            else:
                count[char] = 1
        #go through the 2nd string & decrement/delete the char which is present in dict
        for char in t:
            if char not in count:
                return False
            if count[char]:
                count[char] -= 1
            if count[char] == 0:
                count.pop(char)

        #if the dict is empty return true
        if not count:
            return True
        return False
