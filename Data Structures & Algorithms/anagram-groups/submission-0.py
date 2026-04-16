class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Create a dict
        res = defaultdict(list)
        #loop through the strs dict
        for s in strs:
            #append the strs[i] to the res[strs[i]]
            res["".join(sorted(s))].append(s)
        #return the res in list
        return list(res.values())