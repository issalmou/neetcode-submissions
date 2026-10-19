class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strr={}
        for i in range(len(strs)):
            str_sorted=str(sorted(strs[i]))
            if str_sorted in strr.keys():
                strr[str_sorted].append(strs[i])
            else:
                strr[str_sorted]=[strs[i]]
        return list(strr.values())