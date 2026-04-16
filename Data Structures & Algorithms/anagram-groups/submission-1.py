class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a default dict
        res = defaultdict(list)
        #loop through the string
        for s in strs:
            #create a 26 length list of 0 as counter
            count = [0] * 26
            #for each char in the s:
            for char in s:
                #increament the letter location by 1
                count[ord(char)-ord('a')] += 1
            #append the s to the dict, counter as key
            res[tuple(count)].append(s)
        #return the values of dict values in a list
        return list(res.values())