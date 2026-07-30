class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        #initilise 2 pointers, one at beginining & one at the end
        i=0
        j=len(s)-1
        #while i<j
        while i<j:
            if s[i] == " " or not s[i].isalnum():
                i+=1
                #continue
            elif s[j] == " " or not s[j].isalnum():
                j-=1
                #continue
            elif s[i]!=s[j]:
                print(s[i], s[j])
                return False
            else:
                i+=1
                j-=1
        #true
        return True